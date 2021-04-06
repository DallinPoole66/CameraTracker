'''
Main
Drives the program.
'''
import StepperControl
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(false)

GPIO.setup(enable_pin, GPIO.OUT)
motor_test = StepperControl.StepperMotor(12, 16, 20, 21)
GPIO.setup(enable_pin, 1)

while( True ):
    motor_test.forward(200, 8)
    motor_test.reverse(200, 4)
