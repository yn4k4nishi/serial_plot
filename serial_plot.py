#coding:utf-8
import serial
import numpy as np
import matplotlib.pyplot as plt

##変数の初期化
x_list = [0 for i in range(100)]
y_list = [0 for i in range(100)]

## initialize matplotlib
plt.ion()
plt.figure(figsize=(5,5))
li, = plt.plot(x_list, y_list,"o",color="green")

##グラフの範囲設定
plt.xlim(-10000,10000)
plt.ylim(-10000,10000)

## ポートの指定
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)

x = 0
y = 0

while(1):
    serial = ser.readline().split()
    if len(serial) == 2:
        x = serial[0].decode('utf-8')
        y = serial[1].decode('utf-8')
        print(x,y)
        try:
            x_list.append(float(x))
            x_list.pop(0)
            y_list.append(float(y))
            y_list.pop(0)
        except:
            pass

    li.set_xdata(x_list)
    li.set_ydata(y_list)
    plt.draw()
    plt.pause(.01)

