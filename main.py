'''
Main
Drives the program.
'''
import StepperControl

motor_test = StepperControl.StepperMotor(12, 16, 20, 21)


while( True ):
    motor_test.forward(int((360 / 5.625) * 64))
    motor_test.reverseDirection()