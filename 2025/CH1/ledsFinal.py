import RPi.GPIO as GPIO
import time

# تهيئة وضع GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

# تعريف منافذ الأضواء
LED_R = 17
LED_G = 27
LED_B = 22

Bin_Red=12
Bin_Blue=16
Bin_purple=20


# تهيئة المنافذ كمخرجات
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

GPIO.setup(Bin_Red, GPIO.IN)
GPIO.setup(Bin_Blue, GPIO.IN)
GPIO.setup(Bin_purple, GPIO.IN)
    
red_state=GPIO.HIGH
blue_state=GPIO.HIGH
purple_state=GPIO.HIGH

GPIO.output(LED_R,GPIO.LOW)
GPIO.output(LED_G,GPIO.HIGH)
GPIO.output(LED_B,GPIO.LOW)

try:
    while True:

        red_state=GPIO.input(Bin_Red)
        blue_state=GPIO.input(Bin_Blue)
        purple_state=GPIO.input(Bin_purple)
        
        if(red_state==GPIO.LOW):
            print("red")
            GPIO.output(LED_R,GPIO.HIGH)
            GPIO.output(LED_G,GPIO.LOW)
            GPIO.output(LED_B,GPIO.LOW)
            time.sleep(5)
            print("green")
            GPIO.output(LED_R,GPIO.LOW)
            GPIO.output(LED_G,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.LOW)
            
            
        if(blue_state==GPIO.LOW):
            print("blue")
            GPIO.output(LED_R,GPIO.LOW)
            GPIO.output(LED_G,GPIO.LOW)
            GPIO.output(LED_B,GPIO.HIGH)
            time.sleep(5)
            print("green")
            GPIO.output(LED_R,GPIO.LOW)
            GPIO.output(LED_G,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.LOW)

        if(purple_state==GPIO.LOW):
            print("purple")
            GPIO.output(LED_R,GPIO.HIGH)
            GPIO.output(LED_G,GPIO.LOW)
            GPIO.output(LED_B,GPIO.HIGH)
            time.sleep(5)
            print("green")
            GPIO.output(LED_R,GPIO.LOW)
            GPIO.output(LED_G,GPIO.HIGH)
            GPIO.output(LED_B,GPIO.LOW)
            
        
    
except KeyboardInterrupt: 
    # تنظيف المنافذ في النهاية
    GPIO.cleanup()
    print("GPIO Cleaned")

