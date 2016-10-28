#!/usr/bin/python
# -*- coding: UTF-8 -*-

n = input("多少个数排序：")
book = [0 for i in range(1001)]

for i in range(n):
   t = input("输入要排序的数字：")
   book[t] = book[t]+1

i=1000
while (i>0):
    i=i-1
    j=1
    while(j<=book[i]):
        j=j+1
        print(i)


