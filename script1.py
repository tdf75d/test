import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

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
while 1:
    print('Введите число (-1 для выхода):')
    value=int(input())
    if value==-1:
        break
    else:
        for i in range(8):
            GPIO.setup(convert_pinv(i), GPIO.OUT)
            GPIO.output(convert_pinv(i), 0)
        num2dac(value)
for i in range(8):
            GPIO.setup(convert_pinv(i), GPIO.OUT)
            GPIO.output(convert_pinv(i), 0)