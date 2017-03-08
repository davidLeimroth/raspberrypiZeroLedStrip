#!flask/bin/python3
# -*- coding: utf-8 -*-
# @Author: David Leimroth
# @Date:   2017-02-26 04:23:23
# @Last Modified by:   David Leimroth
# @Last Modified time: 2017-02-26 20:30:38

import wiringpi as wp


R, G, B = 37, 36, 38


def setup():
    print('Starting to set up GPIO\'s')
    wp.wiringPiSetupPhys()
    wp.pinMode(R, 2)
    wp.pinMode(G, 2)
    wp.pinMode(B, 2)
    wp.softPwmCreate(R, 0, 100)  # 5 in app
    wp.softPwmCreate(G, 0, 100)  # 5 in app
    wp.softPwmCreate(B, 0, 100)  # 5 in app
    print('Finished GPIO setup')


def turn_off():
    wp.softPwmWrite(R, 0)
    wp.softPwmWrite(G, 0)
    wp.softPwmWrite(B, 0)


def redPulsing():
    for i in range(50, 255):
        wp.softPwmWrite(R, i)

    for i in reversed(range(50, 255)):
        wp.softPwmWrite(R, i)


def changeingColours():
    for maincolour in range(36, 40):
        nextcolour = maincolour + 1
        if maincolour == 39:
            nextcolour = 36
        # brighten
        for j in range(50, 255):
            wp.softPwmWrite(maincolour, j)
            wp.softPwmWrite(nextcolour, 300 - j)
            wp.delay(1)
        # dimm
        for j in reversed(range(50, 255)):
            wp.softPwmWrite(maincolour, j)
            wp.softPwmWrite(nextcolour, 300 - j)
            wp.delay(1)


def setRed(r_val):
    try:
        wp.softPwmWrite(R, int(r_val))
    except Exception as e:
        print(str(e))    


def setGreen(g_val):
    try:
        wp.softPwmWrite(G, int(g_val))
    except Exception as e:
        print(str(e))    


def setBlue(b_val):
    try:
        wp.softPwmWrite(B, int(b_val))
    except Exception as e:
        print(str(e))    


def manualMode():
    r_val = int(input('RED 0-100> '))
    g_val = int(input('GREEN 0-100> '))
    b_val = int(input('BLUE 0-100> '))
    setRed(r_val)
    setGreen(g_val)
    setBlue(b_val)
    print('Your RGB color is {}, {}, {}'.format(r_val, g_val, b_val))


if __name__ == '__main__':
    setup()
    while True:
        try:
            manualMode()
        except KeyboardInterrupt:
            turn_off()
            print('bye')
            break
        except Exception as e:
            print(str(e))
