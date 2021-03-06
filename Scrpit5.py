import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)
GPIO.setup(4, GPIO.IN)
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
    for i in range(8):
        GPIO.setup(convert_pinv(i), GPIO.OUT)
        GPIO.output(convert_pinv(i), 0)
    if value==-1:
        break
    s=str(value)+' = '+str(round(value/255*3.3, 2)) +'V'
    num2dac(value)
    #if GPIO.input(4)==1:
    #    print('YES')
    print(s)
