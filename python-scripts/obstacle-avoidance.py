from roboclaw_3 import Roboclaw
from time import sleep
import time
import RPi.GPIO as GPIO
import PCF8591 as ADC
import LCD1602 as LCD

# Pin Declarations
F_TRIG = 7  # Front Side Ultrasonic Sensor Trigger Pin
F_ECHO = 12  # Front Side Ultrasonic Sensor Echo Pin
R_TRIG = 40  # Right Side Ultrasonic Sensor Trigger Pin
R_ECHO = 38  # Right Side Ultrasonic Sensor Echo Pin
L_TRIG = 31  # Left Side Ultrasonic Sensor Trigger Pin
L_ECHO = 33  # Left Side Ultrasonic Sensor Echo Pin
G_PIN = 15  # Green LED Pin
R_PIN = 16  # Red LED Pin

# Pins are set according to board pin numbers
GPIO.setmode(GPIO.BOARD)

# Motor Controller Configuration
address = 0x80
roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()

# Setup Function
def setup():
    ADC.setup(0x48)
    GPIO.setup(11, GPIO.IN)
    LCD.init(0x27, 1)

# Rover Direction Functions
def forward():
    roboclaw.ForwardM1(address, 80)
    roboclaw.ForwardM2(address, 80)

def backward():
    roboclaw.BackwardM1(address, 80)
    roboclaw.BackwardM2(address, 80)

def left_rotate():
    roboclaw.ForwardM1(address, 80)
    roboclaw.BackwardM2(address, 80)

def right_rotate():
    roboclaw.BackwardM1(address, 80)
    roboclaw.ForwardM2(address, 80)

def stop():
    roboclaw.ForwardM1(address, 0)
    roboclaw.BackwardM2(address, 0)

# Left side Distance Function
def left_distance():
    while True:
        GPIO.setup(L_TRIG, GPIO.OUT)
        GPIO.setup(L_ECHO, GPIO.IN)
        GPIO.output(L_TRIG, False)
        time.sleep(0.01)
        GPIO.output(L_TRIG, True)

        time.sleep(0.00001)

        GPIO.output(L_TRIG, False)
        l_pulse_start = time.time()
        timeout = l_pulse_start + 0.04
        while GPIO.input(L_ECHO) == 0 and l_pulse_start < timeout:
            l_pulse_start = time.time()

        l_pulse_end = time.time()
        timeout = l_pulse_end + 0.04
        while GPIO.input(L_ECHO) == 1 and l_pulse_end < timeout:
            l_pulse_end = time.time()

        l_pulse_duration = l_pulse_end - l_pulse_start
        left_dist = l_pulse_duration * 17150

        return left_dist

# Right side Distance Function
def right_distance():
    while True:
        GPIO.setup(R_TRIG, GPIO.OUT)
        GPIO.setup(R_ECHO, GPIO.IN)
        GPIO.output(R_TRIG, False)
        time.sleep(0.01)
        GPIO.output(R_TRIG, True)

        time.sleep(0.00001)

        GPIO.output(R_TRIG, False)
        r_pulse_start = time.time()
        timeout = r_pulse_start + 0.04
        while GPIO.input(R_ECHO) == 0 and r_pulse_start < timeout:
            r_pulse_start = time.time()

        r_pulse_end = time.time()
        timeout = r_pulse_end + 0.04
        while GPIO.input(R_ECHO) == 1 and r_pulse_end < timeout:
            r_pulse_end = time.time()

        r_pulse_duration = r_pulse_end - r_pulse_start
        right_dist = r_pulse_duration * 17150

        return right_dist

# Obstacle Avoidance Function
def obstacle_avoidance():
    while True:
        print("Distance measurement in progress")
        GPIO.setup(F_TRIG, GPIO.OUT)
        GPIO.setup(F_ECHO, GPIO.IN)
        GPIO.output(F_TRIG, False)
        time.sleep(0.01)
        GPIO.output(F_TRIG, True)

        time.sleep(0.00001)

        GPIO.output(F_TRIG, False)
        f_pulse_start = time.time()
        timeout = f_pulse_start + 0.04
        while GPIO.input(F_ECHO) == 0 and f_pulse_start < timeout:
            f_pulse_start = time.time()

        f_pulse_end = time.time()
        timeout = f_pulse_end + 0.04
        while GPIO.input(F_ECHO) == 1 and f_pulse_end < timeout:
            f_pulse_end = time.time()

        f_pulse_duration = f_pulse_end - f_pulse_start
        forward_dist = f_pulse_duration * 17150
        left = left_distance()
        right = right_distance()
        print("Forward Distance:", forward_dist, "cm")
        print("Left Distance:", left, "cm")
        print("Right Distance:", right, "cm")

        if forward_dist > 20 and left > 10 and right > 10:
            forward()
        elif forward_dist < 20 or left < 20 or right < 20:
            left = left_distance()
            right = right_distance()
            print("Left Distance:", left, "cm")
            print("Right Distance:", right, "cm")

            if forward_dist < 20 and left > 20 and right > 20:
                left_rotate()
                sleep(0.3)
            if left > 20 and right < 20:
                left_rotate()
                sleep(0.3)
            if left < 20 and right > 20:
                right_rotate()
                sleep(0.3)
            if left < 15 and right < 15:
                backward()
                right_rotate()
            sleep(0.5)

if __name__ == '__main__':
    try:
        setup()
        obstacle_avoidance()
    except KeyboardInterrupt:
        stop()
        pass
