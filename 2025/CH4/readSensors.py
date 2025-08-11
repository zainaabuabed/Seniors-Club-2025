import RPi.GPIO as GPIO
import time

left1Sensor = 27   
left2Sensor = 22  
right1Sensor = 17  
right2Sensor = 4

def hardware_Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(left1Sensor,GPIO.IN)
    GPIO.setup(left2Sensor,GPIO.IN)
    GPIO.setup(right1Sensor,GPIO.IN)
    GPIO.setup(right2Sensor,GPIO.IN)
    
def read_Sensors():
    l1 = GPIO.input(left1Sensor) # left 1 sensor value
    l2= GPIO.input(left2Sensor)  # left 2 sensor value
    r1 = GPIO.input(right1Sensor) # right 1 sensor value
    r2 = GPIO.input(right2Sensor) # right 2 sensor value
    return[l1,l2,r1,r2]


try:
    while True:
        hardware_Setup()
        Sensors_Values=read_Sensors()
        print (Sensors_Values)
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    