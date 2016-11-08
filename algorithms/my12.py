#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 冒泡排序演示

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score


students = [Student('huhu',5),Student('haha',3),Student('xixi',5), Student('hengheng',2), Student('gaoshou',8)]



# n = input ("输入一个数")
#
# for i in range(n):
#     s = Student(input("输入名称"), input("输入成绩"))
#     students.append(s)
#

n = len(students)

for i in range(n):
    for j in range(n-i-1):
        if(students[j].score <students[j+1].score):
            students[j], students[j+1] = students[j+1], students[j]

print('###############')
for i in range(n):
         print(students[i].name+':'+ str(students[i].score))
print('###############')

###############
# gaoshou
# huhu
# xixi
# haha
# hengheng
###############