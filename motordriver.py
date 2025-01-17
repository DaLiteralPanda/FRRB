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

# Turn left
def left(sec):
    print("Turning left")
    gpio.output(17, False)  # Stop or reverse left motor
    gpio.output(22, False)
    gpio.output(23, True)   # Move right motor forward
    gpio.output(24, False)
    time.sleep(sec)

# Turn right
def right(sec):
    print("Turning right")
    gpio.output(17, True)   # Move left motor forward
    gpio.output(22, False)
    gpio.output(23, False)  # Stop or reverse right motor
    gpio.output(24, False)
    time.sleep(sec)

# Cleanup GPIO
def cleanup():
    gpio.cleanup()
    print("GPIO cleanup complete")

# Main program
try:
    init()
    print("Starting motor test")
    forward(2)  # Move forward for 2 seconds
    left(1)     # Turn left for 1 second
    forward(2)  # Move forward for 2 seconds
    right(1)    # Turn right for 1 second
    reverse(2)  # Move backward for 2 seconds
finally:
    cleanup()
