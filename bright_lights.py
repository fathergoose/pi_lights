import RPi.GPIO as GPIO
import time

led_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

def blink(times, speed):
    i = 0
    while i < times:
        GPIO.output(led_pin, True)
        time.sleep(speed)
        GPIO.output(led_pin, False)
        time.sleep(speed)
        i = i + 1
    #GPIO.cleanup()

# blink(5, .2)

while True:
    duty_s = input("% Brightness? ")
    duty = int(duty_s)
    pwm_led.ChangeDutyCycle(duty)

