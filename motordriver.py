import RPi.GPIO as gpio
import time

# Initialize GPIO pins
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)  # IN1
    gpio.setup(22, gpio.OUT)  # IN2
    gpio.setup(23, gpio.OUT)  # IN3
    gpio.setup(24, gpio.OUT)  # IN4

# Move forward
def forward(sec):
    print("Moving forward")
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(sec)

# Move reverse
def reverse(sec):
    print("Moving reverse")
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(sec)

# Cleanup GPIO
def cleanup():
    gpio.cleanup()
    print("GPIO cleanup complete")

# Main program
try:
    init()
    print("Starting motor test")
    forward(4)
    time.sleep(1)
    reverse(4)
finally:
    cleanup()
