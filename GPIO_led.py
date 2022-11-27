# import GPIO library
import Jetson.GPIO as GPIO

# import time library
import time

# set Pin number
pin1 = 22
pin2 = 18

# set GPIO mode
GPIO.setmode(GPIO.BOARD)

# set initial pin signal
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)

# LED states are switched every 2 seconds
print('press ctrl+c to exit')
try:
    while True:
        time.sleep(2)
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
        time.sleep(2)
        GPIO.output(pin2, GPIO.HIGH)
        GPIO.output(pin1, GPIO.LOW)
except KeyboardInterrupt:
    pass

# turn off led after operation
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)

# clean resource
GPIO.cleanup()
