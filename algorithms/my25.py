#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 模拟链表

n =9

data = [0, 2,3,5,8,9,10,18,26,32,6]
right =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(1, 10):
    if(i!=n):
        right[i]=i+1
    else:
        right[i]=0

t=1
len = n +1
while t!=0:
    if(data[right[t]]>data[len]):
        right[len]=right[t]
        right[t] = len
        break

    t = right[t]

#输出链表中所有的数

t=1

while(t!=0):
    print(data[t])
    t=right[t]

