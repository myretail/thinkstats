#!/usr/bin/python

# 火柴棍等式

def fun(x):
    num =0
    f=[6,2,5,5,4,5,6,3,7,6]

    while(int(x/10)!=0):
        num = num + f[int(x%10)]
        x=int(x/10)

    num = num + f[int(x)]

    return num

m = 18
sum =0
for a in range (1112):
    for b in range(1112):
        c=a+b
       # print("%d+%d=%d" % (a,b,c))
        if(fun(a)+fun(b)+fun(c) == m-4):
            print("结果是： %d+%d=%d" % (a,b,c))
            sum = sum +1

print ("一空可以拼出%d个不同的等式" %(sum))

