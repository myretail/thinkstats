#!/usr/bin/python


n =13
m =13

a =  [['#' for col in range(n)] for row in range(m)]
map=0
# init G
for i in [1,2,4,5,6,8,9,10]:
    a[1][i]='G'
for i in [5,7,9,11]:
    a[2][i]='G'
for i in [11]:
    a[3][i]='G'
for i in [1,9,11]:
    a[4][i]='G'
for i in [1,2,4,5,6,10,11]:
    a[5][i]='G'
for i in [1,5]:
    a[6][i]='G'
for i in [2,6]:
    a[7][i]='G'
for i in [1,5,11]:
    a[8][i]='G'
for i in [4,6,7,8,10,11]:
    a[9][i]='G'
for i in [1,5,7,11]:
    a[10][i]='G'
for i in [1,2,4,5,6,8,10,11]:
    a[11][i]='G'



# init .
for i in [3,11]:
    a[1][i]='.'
for i in [3]:
    a[2][i]='.'
for i in [1,2,3,4,5,6,7,9,10]:
    a[3][i]='.'
for i in [3,7]:
    a[4][i]='.'
for i in [3,7,9]:
    a[5][i]='.'
for i in [3,7,9]:
    a[6][i]='.'
for i in [3,4,5,7,8,9,10,11]:
    a[7][i]='.'
for i in [3,9]:
    a[8][i]='.'
for i in [1,2,3,9]:
    a[9][i]='.'
for i in [3,9]:
    a[10][i]='.'
for i in [3,9]:
    a[11][i]='.'

for i in range(13):
    for j in range(13):
        if(a[i][j]=='.'):
            sum =0
            x=i
            y=j
            while(a[x][y]!='#'):
                if(a[x][y]=='G'):
                    sum = sum +1
                x = x -1

            x = i
            y=j
            while(a[x][y]!='#'):
               # print (a[x][y])
                if(a[x][y]=='G'):
                    sum = sum +1
                x=x+1


            x=i
            y=j
            while(a[x][y]!='#'):
                if(a[x][y]=='G'):
                    sum = sum +1
                y = y -1


            x=i
            y=j
            while(a[x][y]!='#'):
                if(a[x][y]=='G'):
                    sum = sum +1
                y = y +1


            # print ("sum= %d" % (sum))
            if(sum>map):
                map = sum
                p=i
                q=j

print ("将炸弹放置在(%d, %d),最多可以消灭%d个敌人" % (p, q, map))
