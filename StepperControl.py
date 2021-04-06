'''
Stepper motor Object
'''

import RPi.GPIO as GPIO
import time

class StepperMotor():
    SEQ = list(8)
    SEQ[0] = [0,1,0,0]
    SEQ[1] = [0,1,0,1]
    SEQ[2] = [0,0,0,1]
    SEQ[3] = [1,0,0,1]
    SEQ[4] = [1,0,0,0]
    SEQ[5] = [1,0,1,0]
    SEQ[6] = [0,0,1,0]
    SEQ[7] = [0,1,1,0]

    in_1 = None
    in_2 = None
    in_3 = None
    in_4 = None

    def __init__(self, pin_1, pin_2, pin_3, pin_4):
        self.in_1 = pin_1
        self.in_2 = pin_2
        self.in_3 = pin_3
        self.in_4 = pin_4
        
        GPIO.setup(self.in_1, GPIO.OUT)
        GPIO.setup(self.in_2, GPIO.OUT)
        GPIO.setup(self.in_3, GPIO.OUT)
        GPIO.setup(self.in_4, GPIO.OUT)


    def set_step(self, p1, p2, p3, p4):
        GPIO.output(self.in_1, p1)
        GPIO.output(self.in_2, p2)
        GPIO.output(self.in_3, p3)
        GPIO.output(self.in_4, p4)

    def forward(self, delay, steps):
        for _ in range(steps):
            for i in range(8):
                self.set_step(self.SEQ[i][0], self.SEQ[i][1], self.SEQ[i][2], self.SEQ[i][3] )
                time.sleep(delay)

    def reverse(self, delay, steps):
        for _ in range(steps):
            for i in reversed(range(8)):
                self.set_step(self.SEQ[i][0], self.SEQ[i][1], self.SEQ[i][2], self.SEQ[i][3] )
                time.sleep(delay)


