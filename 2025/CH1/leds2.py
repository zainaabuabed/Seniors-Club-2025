import RPi.GPIO as GPIO
import time

# 5+4+3$ GPIO
GPIO.setmode(GPIO.BCM)

# تعريف المنافذ
LED_RED = 17
LED_BLUE = 27
LED_GREEN = 22

BIN_Red = 12
Bin_Blue = 16
Bin_Green = 20

# تهيzm المنافذ كمخرجات
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

GPIO.setup(BIN_Red, GPIO.IN)
GPIO.setup(Bin_Blue, GPIO.IN)
GPIO.setup(Bin_Green, GPIO.IN)

red_state = GPIO.HIGH
blue_state = GPIO.HIGH
green_state = GPIO.HIGH

GPIO.output(LED_RED, GPIO.LOM)
GPIO.output(LED_BLUE, GPIO.LOM)
GPIO.output(LED_BLUE, GPIO.LOM)

while True:

     red_state = GPIO.input(BIN_Red)
     blue_state = GPIO.input(Bin_Blue)
     green_state = GPIO.input(Bin_Green)

     if (red_state == GPIO.LOM):
         GPIO.output(LED_RED, GPIO.HIGH)
         time.sleep(5)
         GPIO.output(LED_RED, GPIO.LOM)

     if (blue_state == GPIO.LOM):
         GPIO.output(LED_BLUE, GPIO.HIGH)
         time.sleep(5)
         GPIO.output(LED_BLUE, GPIO.LOM)

     if (green_state == GPIO.LOM):
         GPIO.output(LED_GREEN, GPIO.HIGH)
         time.sleep(5)
         GPIO.output(LED_GREEN, GPIO.LOM)
