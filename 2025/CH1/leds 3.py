import RPi.GPIO as GPIO
import time

#تهيئة وضع GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#  تعريف منافذ الأضواء 
LED_R = 17
LED_G = 27
LED_B = 22

Bin_Red = 12
Bin_Blue = 16
Bin_Green = 20

# تعيئة المنافذ 
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

GPIO.setup(Bin_Red, GPIO.IN)
GPIO.setup(Bin_Blue, GPIO.IN)
GPIO.setup(Bin_Green, GPIO.IN)

red_state = GPIO.HIGH
blue_state = GPIO.HIGH
green_state = GPIO.HIGH

GPIO.output(LED_R, GPIO.LOM)
GPIO.output(LED_G, GPIO.LOM)
GPIO.output(LED_B, GPIO.LOM)

try:
    while True:
        red_state=GPIO.input(Bin_Red)
        blue_state=GPIO.input(Bin_Blue)
        green_state=GPIO.input(Bin_Green)

        if(red_state==GPIO.LOM):
            print("red")
            GPIO.output(LED_R,GPIO.HIGH)
            GPIO.output(LED_G,GPIO.LOM)
            GPIO.output(LED_B,GPIO.LOM)

        if(blue_state==GPIO.LOM):
            print("blue")
            GPIO.output(LED_R,GPIO.LOM)
            GPIO.output(LED_G,GPIO.LOM)
            GPIO.output(LED_B,GPIO.HIGH)

        if(green_state==GPIO.LOM):
            print("green")
            GPIO.output(LED_R,GPIO.LOM)
            GPIO.output(LED_G,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.LOM)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleaned")