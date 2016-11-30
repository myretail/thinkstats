#!/usr/bin/python

#图的遍历，广度优先

e = [[99999999 for col in range(101)] for row in range(101)]

e[1][2] = 1
e[2][1] = 1

e[1][3] = 1
e[3][1] = 1

e[1][5] = 1
e[5][1] = 1

e[2][4] = 1
e[4][2] = 1

# e[3][5]=1
# e[5][3]=1


n = 5
m = 5

book = [0 for col in range(101)]
que = {}

head = 1
tail = 1

que[tail] = 1
tail += 1
book[1] = 1

while head < tail:
    cur = que[head]
    for j in range(n + 1):
        i = j + 1
        if e[cur][i] == 1 and book[i] == 0:
            que[tail] = i
            tail += 1
            book[i] = 1

        if tail > n:
            break
    head += 1

print(*que.values(), sep=' ')
