#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: David Leimroth
# @Date:   2017-02-26 03:00:46
# @Last Modified by:   David Leimroth
# @Last Modified time: 2017-02-26 15:12:43

import RPi.GPIO as GPIO
from time import sleep

R = 37
G = 36
B = 38


def turn_off():
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.cleanup()


def setup(freq):
    print('Starting Setup')
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    pR = GPIO.PWM(R, freq)
    pG = GPIO.PWM(G, freq)
    pB = GPIO.PWM(B, freq)
    print('Finished Setup')
    return pR, pG, pB


# def loop(pR, pG, pB):
    # pR.start(0)
    # pG.start(0)
    # pB.start(0)
def loop(*args):
    for arg in args:
        arg.start(0)
    try:
        arg = args[0]
        while True:

            # for arg in args:
            for j in range(100):
                arg.ChangeDutyCycle(j)
                sleep(0.01)
            for j in range(100):
                arg.ChangeDutyCycle(100 - j)
                sleep(0.01)

    except Exception as e:
        for arg in args:
            arg.stop()
            GPIO.cleanup()
        print(str(e))


if __name__ == '__main__':
    pR, pB, pG = setup(60)
    # while True:
    #     loop
    loop(pR, pG, pB)
    # turn_off()


def test_loop():
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    sleep(2)
    GPIO.output(B, GPIO.LOW)
    sleep(2)
    GPIO.output(R, GPIO.LOW)
    sleep(2)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(G, GPIO.LOW)
    sleep(1)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(R, GPIO.HIGH)
