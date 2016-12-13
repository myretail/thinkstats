#!/usr/bin/python

# sort

h = [0, 99, 5, 36, 7, 22, 17, 46, 12, 2, 19, 25, 28, 1, 92]

num = 14
n = num


def swap(x, y):
    global h
    h[x], h[y] = h[y], h[x]


def siftdown(i):
    global n, h
    flag = 0

    while i * 2 <= n and flag == 0:
        if h[i] < h[i * 2]:
            t = i * 2
        else:
            t = i

        if i * 2 + 1 <= n:
            if h[t] < h[i * 2 + 1]:
                t = i * 2 + 1

        if t != i:
            swap(t, i)
            i = t
        else:
            flag = 1


def creat():
    global n

    for i in range(int(n / 2), 0, -1):
        siftdown(i)


def heapsort():
    global n
    while n > 1:
        swap(1, n)
        n = n - 1
        siftdown(1)


creat()

heapsort()

for i in range(1, num + 1):
    print(h[i])
