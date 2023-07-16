# 이제 지정한 좌표로 이동하게 만들자! - 0716
# 방향전환 각도 표시에 문제 있음

import numpy as np
import matplotlib.pyplot as plt
import serial,time

# py_serial = serial.Serial("COM5",baudrate=9600)
# n = 2 # sqrt number
# num = 10 # x_axis range
flag=0
pre_x = 1
pre_y = 1
mmap = np.array([[0,0,0],
                 [0,0,0],
                 [0,0,0]])
mmap[1,1] = 1 # 위치 초기화

# for i in range(len(mmap)):
#     for n in range(len(mmap[i])):
#         if mmap[i][n] == 1: 
#             flag = 1
#             break
#     if flag == 1: break
    
# def sqrt_x(n, num): # sqrt num, x_axis range # n차함수 그리는 로봇에 사용
#     arr = []
#     for i in range(num):
#         arr.append((i-num)**n)
#     for i in range(num+1):
#         arr.append(i**n)
#     return arr

# def x_axis(n, num): # sqrt num, x_axis range # n차함수 그리는 로봇에 사용
#     length = []
#     for i in range(num):
#         length.append(-len(sqrt_x(n,num))//2 + (i+1))
#     for i in range(num+1):
#         length.append(i)
#     return length

def move(i,n): #이동 기능
    mmap = np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0]])
    mmap[i][n] = 1  
    return mmap
print(f"{mmap}   STARTING MAP")

def move_process(i,n):
    global mmap
    global com_map
    com_map = mmap
    mmap = move(i,n)
    
def X_Y_move(mmap):
    global pre_x
    global pre_y
    global x_angle_val
    global y_angle_val
    x_angle_val = 0
    y_angle_val = 0
    x_axis = np.where(mmap == 1)[1][0]
    y_axis = np.where(mmap == 1)[0][0]
    print(f"MOVE : {pre_x - x_axis}  {pre_y - y_axis}")
    if pre_x - x_axis == 0: x_angle_val = 0
    elif pre_x - x_axis > 0: x_angle_val = 'LEFT'
    elif pre_x - x_axis < 0: x_angle_val = 'RIGHT'
    if pre_y - y_axis == 0: y_angle_val = 0
    elif pre_y - y_axis > 0: y_angle_val = 'UP'
    elif pre_y - y_axis < 0: y_angle_val = 'DOWN'

    print(f"ANGLE : X : {x_angle_val}  Y : {y_angle_val}")
    pre_x = x_axis
    pre_y = y_axis
    print(x_axis, y_axis)
    
def angle(x_angle_val,y_angle_val):
    x_angle = 0
    y_angle = 0
    if x_angle_val == 'LEFT': x_angle = -90
    elif x_angle_val == 'RIGHT': x_angle = 90
    if y_angle_val == 'UP': y_angle = 90
    elif y_angle_val == 'DOWN': y_angle = -90
    
    if abs(x_angle) == abs(y_angle): 
        if x_angle < 0 or y_angle < 0: return -(abs(x_angle) + abs(y_angle))//4
        elif x_angle > 0 or y_angle > 0: return (x_angle + y_angle)//4
    else: return x_angle + y_angle

    
while True:
    i,n = map(int,input().split())
    move_process(i,n)
    print(mmap)
    X_Y_move(mmap)
    print(angle(x_angle_val,y_angle_val))
    
    
    # if move_value(mmap) == -3: py_serial.write(str('a').encode())
    # if move_value(mmap) == 3: py_serial.write(str('b').encode())
    # if move_value(mmap) == 1: py_serial.write(str('c').encode())
    # if move_value(mmap) == -1: py_serial.write(str('d').encode())
    
# plt.plot(x_axis(n,num),sqrt_x(n,num))
# plt.show()

