from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i1= 18
i2= 17


def setServoAngle(servo, angle):
    pwm = GPIO.PWM(servo, 30)
    pwm.start(8)

    GPIO.output(i1,0)
    GPIO.output(i2,1)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.3)
    pwm.stop()

if __name__ == '__main__':
    import sys
    servo = int(sys.argv[1])
    GPIO.setup(servo, GPIO.OUT)
    GPIO.setup(i1,GPIO.OUT)
    GPIO.setup(i2,GPIO.OUT)
    setServoAngle(servo, int(sys.argv[2]))
    GPIO.cleanup()