#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 快速排序演示

a = [0, 6,1,2,7,9,3,4,5,10,8]


def QuickSort(left, right):
    if(left>right):
        return

    temp =a[left]
    i=left
    j=right

    while(i!=j):
        while(a[j]>=temp and i<j):
            j=j-1

        while(a[i]<=temp and i<j):
            i = i +1

        if(i<j):
            a[i],a[j]=a[j],a[i]

    a[left]=a[i]
    a[i]=temp

    QuickSort(left, i-1)
    QuickSort(i+1,right)

QuickSort(1,10)

for i in range(10):
    print(a[i+1])


# 输出
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
