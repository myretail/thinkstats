#!/usr/bin/python

#  深度优先

a = [0 for i in range(10)]

book = [0 for i in range(10)]

total =0

def dfs(step):
    global total
    if(step==10):
        if(a[1]*100+a[2]*10+a[3]+a[4]*100+a[5]*10+a[6] == a[7]*100 + a[8]*10 + a[9]):
            total = total +1
            print('%d%d%d+%d%d%d=%d%d%d\n' % (a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
        return

    for i in range(1,10):
        if(book[i]==0):
            a[step] = i
            book[i]=1
            dfs(step+1)
            book[i]=0
    return 

dfs(1)

print("total=%d" % (total/2))



