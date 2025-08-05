import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Define LED pins
LED_RED = 17
LED_BLUE = 27
LED_GREEN = 22

# Initialize pins as outputs
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

try:
    # Turn on LEDs with delays
    GPIO.output(LED_RED, GPIO.HIGH)  # Turn on red LED
    time.sleep(2)                    # Wait 2 seconds
    GPIO.output(LED_BLUE, GPIO.HIGH) # Turn on blue LED
    time.sleep(2)                    # Wait 2 seconds
    GPIO.output(LED_GREEN, GPIO.HIGH) # Turn on green LED
    time.sleep(5)                    # Wait 5 seconds
    
    # Turn off all LEDs (corrected from LOM to LOW)
    GPIO.output(LED_RED, GPIO.LOW)   # Turn off red LED
    GPIO.output(LED_BLUE, GPIO.LOW)  # Turn off blue LED
    GPIO.output(LED_GREEN, GPIO.LOW) # Turn off green LED

finally:
    # Clean up GPIO ports
    GPIO.cleanup()
    print("GPIO ports cleaned up")