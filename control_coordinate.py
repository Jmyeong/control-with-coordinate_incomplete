import numpy as np
import serial

py_serial = serial.Serial("COM5",baudrate=9600)
n = 2 # sqrt number
num = 10 # x_axis range
flag=0

mmap = np.array([[0,0,0],
                 [0,0,0],
                 [0,0,0]])
mmap[1,1] = 1 # 위치 초기화
def angle(angle):
    return angle //90

def move(i,n): #이동 기능
    mmap = np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0]])
    mmap[i][n] = 1  
    return mmap
print(f"{mmap}   STARTING MAP")
def move_value(mmap):
    flag1=0
    flag2=0
    
    global com_map
    for i in range(len(mmap)):
        for n in range(len(mmap[i])):
            flag1 += 1
            if (mmap-com_map)[i][n] == 1: break
        if (mmap-com_map)[i][n] == 1: break
    for i in range(len(mmap)):
        for n in range(len(mmap[i])):
            flag2 += 1
            if (mmap-com_map)[i][n] == -1: break
        if (mmap-com_map)[i][n] == -1: break
    return flag1-flag2

def move_process(i,n):
    global mmap
    global com_map
    com_map = mmap
    mmap = move(i,n)
    
    

while True:
    i,n = map(int,input().split())
    move_process(i,n)
    print(f"Move value : {move_value(mmap)}")
    print(mmap)
    # -------------------------------------------------------------- to arduino
    # if move_value(mmap) == -3: py_serial.write(str('a').encode())
    # if move_value(mmap) == 3: py_serial.write(str('b').encode())
    # if move_value(mmap) == 1: py_serial.write(str('c').encode())
    # if move_value(mmap) == -1: py_serial.write(str('d').encode())
    # ---------------------------------------------------------------
    


