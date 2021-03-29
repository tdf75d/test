import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import numpy
import matplotlib.pyplot as plt

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
def sin(t,frequancy,samplingFrequancy):
    x=[]
    i=0
    while i<=t:
        x.append(i*frequancy)
        i+=1/samplingFrequancy
    for p in range(len(x)):
        x[p]=x[p]*2*numpy.pi*frequancy
    y=numpy.sin(x)
    for i in range(len(y)):
        y[i]=1.65+1.65*y[i]
    for j in range(len(x)):
        num2dac(round(y[j]*256/3.3))
        time.sleep(1/samplingFrequancy)
        for k in range(8):
                GPIO.setup(convert_pinv(k), GPIO.OUT)
                GPIO.output(convert_pinv(k), 0)
    return x,y
t=int(input())
frequancy=int(input())
samplingFrequancy=int(input())
x,y=sin(t,frequancy,samplingFrequancy)
plt.plot(x,y)
plt.show()