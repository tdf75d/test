#import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, GPIO.OUT)
# GPIO.output(17, 1)
# GPIO.setup(4, GPIO.IN)


def convert_pinv(n):
    if n == 0:
        return 10
    if n == 1:
        return 9
    if n == 2:
        return 11
    if n == 3:
        return 5
    if n == 4:
        return 6
    if n == 5:
        return 13
    if n == 6:
        return 19
    if n == 7:
        return 26


def decToBinList(decNumber):
    s = str(bin(decNumber))
    s = s[2:]
    s = str(0) * (8 - len(s)) + s
    arr = [0] * 8
    for i in range(8):
        arr[i] = int(s[i])
    return arr


def num2dac(number):
    arr = decToBinList(number)
    for i in range(8):
        if arr[i]:
            ledNumber = convert_pinv(7 - i)
            GPIO.setup(ledNumber, GPIO.OUT)
            GPIO.output(ledNumber, 1)


def acp(a=0):
    for j in range(256):
        for i in range(8):
            GPIO.setup(convert_pinv(i), GPIO.OUT)
            GPIO.output(convert_pinv(i), 0)
        num2dac(j)
        time.sleep(0.001)
        if GPIO.input(4) == 0:
            print(round(j / 255 * 3.3, 2))
            return


def binacp1():
    l = 0
    r = 255
    lv = None
    rv = None
    jv = None
    for i in range(8):
        GPIO.setup(convert_pinv(i), GPIO.OUT)
        GPIO.output(convert_pinv(i), 0)
    num2dac(l)
    time.sleep(0.001)
    lv = GPIO.input(4)
    for i in range(8):
        GPIO.setup(convert_pinv(i), GPIO.OUT)
        GPIO.output(convert_pinv(i), 0)
    num2dac(r)
    time.sleep(0.001)
    rv = GPIO.input(4)
    while 1:
        if r >= 128:
            j = (l + r) // 2 + 1
        else:
            j = (l + r) // 2
        for i in range(8):
            GPIO.setup(convert_pinv(i), GPIO.OUT)
            GPIO.output(convert_pinv(i), 0)
        num2dac(j)
        time.sleep(0.001)
        jv = GPIO.input(4)
        if r - l > 0:
            if jv != lv:
                r = j
                rv = jv
            elif jv != rv:
                l = j
                lv = jv
        else:
            print(round(((r + l) // 2) / 255 * 3.3, 2))
            return


for i in range(8):
    GPIO.setup(convert_pinv(i), GPIO.OUT)
    GPIO.output(convert_pinv(i), 0)


def binacp2():
    l = -1
    r = 256
    lv = None
    rv = None
    jv = None
    lv = 1
    for i in range(8):
        GPIO.setup(convert_pinv(i), GPIO.OUT)
        GPIO.output(convert_pinv(i), 0)
    num2dac(r)
    time.sleep(0.001)
    rv = 0
    while 1:
        j = (l + r+1) // 2
        for i in range(8):
            GPIO.setup(convert_pinv(i), GPIO.OUT)
            GPIO.output(convert_pinv(i), 0)
        num2dac(j)
        time.sleep(0.001)
        jv = int(GPIO.input(4))
        print(rv)
        if r - l >1:
            if jv != lv:
                r = j
                rv = jv
            elif jv != rv:
                l = j
                lv = jv
        else:
            print(round((j / 255 * 3.3, 2))
            return


for i in range(8):
    GPIO.setup(convert_pinv(i), GPIO.OUT)
    GPIO.output(convert_pinv(i), 0)

binacp2(v)