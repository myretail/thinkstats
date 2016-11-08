#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 小猫钓鱼

# 这个在官网中list支持，有实现。
#
# 补充一下栈，队列的特性：
#
# 1.栈(stacks)是一种只能通过访问其一端来实现数据存储与检索的线性数据结构，具有后进先出(last in first out，LIFO)的特征
#
# 2.队列(queue)是一种具有先进先出特征的线性数据结构，元素的增加只能在一端进行，元素的删除只能在另一端进行。能够增加元素的队列一端称为队尾，可以删除元素的队列一端则称为队首。
#
# 地址在 http://docs.python.org/2/tutorial/datastructures.html#more-on-lists ，下面的官方的代码。
#
# 关于栈
# >>> stack = [3, 4, 5]
# >>> stack.append(6)
# >>> stack.append(7)
# >>> stack
# [3, 4, 5, 6, 7]
# >>> stack.pop()
# 7
# >>> stack
# [3, 4, 5, 6]
# >>> stack.pop()
# 6
# >>> stack.pop()
# 5
# >>> stack
# [3, 4]
#
# 关于队列
# >>> from collections import deque
# >>> queue = deque(["Eric", "John", "Michael"])
# >>> queue.append("Terry")           # Terry arrives
# >>> queue.append("Graham")          # Graham arrives
# >>> queue.popleft()                 # The first to arrive now leaves
# 'Eric'
# >>> queue.popleft()                 # The second to arrive now leaves
# 'John'
# >>> queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])
#
# 上面代码很清晰的解释了上面的2种结构

from collections import deque

q1 = deque([2, 4, 1, 2, 5, 6])
q2 = deque([3, 1, 3, 5, 6, 4])

s = []

book = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while len(q1) > 0 and len(q2) > 0:
    t = q1.popleft()
    if book[t] == 0:
        s.append(t)
        book[t] = 1
    else:
        q1.append(t)
        temp = s.pop()
        while temp != t:
            book[temp] = 0
            q1.append(temp)
            temp = s.pop()
        s.append(temp)  # 在上面循环中多pop了一次

    t = q2.popleft()
    if book[t] == 0:
        s.append(t)
        book[t] = 1
    else:
        q2.append(t)
        temp = s.pop()
        while temp != t:
            book[temp] = 0
            q2.append(temp)
            temp = s.pop()
        # 在上面循环中多pop了一次
        s.append(temp)

if len(q2) == 0:
    print("小哼win")
    print("小哼的牌：" + str(q1))

    print("桌子上的牌：" + str(s))


else:
    print("小哈win")
    print("小哈的牌：" + str(q2))

    print("桌子上的牌：" + str(s))
