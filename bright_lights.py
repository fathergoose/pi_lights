import RPi.GPIO as GPIO
import time
import resistance

led_pin = 4
CALIBRATION = 300 # maximum MEASURED value of resistance.read_pot()

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(0)

def blink(times, speed):
    i = 0
    while i < times:
        GPIO.output(led_pin, True)
        time.sleep(speed)
        GPIO.output(led_pin, False)
        time.sleep(speed)
        i = i + 1

# blink(5, .2)

while True:
    pot = resistance.read_pot()
    duty = pot // 10
    pwm_led.ChangeDutyCycle(duty)
    time.sleep(.1)
    
    # duty_s = input("% Brightness? ")
    # duty = int(duty_s)
    # pwm_led.ChangeDutyCycle(duty)

GPIO.cleanup()
