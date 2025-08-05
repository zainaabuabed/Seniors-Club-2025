import time
import RPi.GPIO as GPIO
from Sensors import Buzzer
buzzer=Buzzer(32)

try:
  buzzer.beep()
except KeyboardInterrupt:
    buzzer.close()
    GPIO.cleanup()
finally:
    buzzer.close()
    GPIO.cleanup()

