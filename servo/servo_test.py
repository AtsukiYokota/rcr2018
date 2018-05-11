#!/usr/bin/env python3
import pigpio
import time

PWM_PIN = 18

PERIOD = 20
STOP_WIDTH = 1.5

def period2freq(period):
    return 1000 / period

def width2duty(width, period):
    return (width / period) * 1000000.0

try:
    pi = pigpio.pi()

    pi.set_mode(PWM_PIN, pigpio.OUTPUT)

    while True:
        # neutral
        print('Neutral')
        pi.hardware_PWM(PWM_PIN, period2freq(PERIOD), width2duty(STOP_WIDTH))
        time.sleep(3)
        # CW
        pi.hardware_PWM(PWM_PIN, period2freq(PERIOD), width2duty(0.9))
        time.sleep(3)
        # CCW
        pi.hardware_PWM(PWM_PIN, period2freq(PERIOD), width2duty(2.1))
        time.sleep(3)

except KeyboardInterrupt:
    pi.set_mode(PWM_PIN, pigpio.INPUT)
    pi.stop()
    exit(0)
