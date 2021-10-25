#Atousa-Niazi-Abkoh-98440127-Python-checkerboard page-OSLab-T4.2


print('enter n for rows:')
n=int(input())
print('enter m for colums:')
m=int(input())

x = [[ 0 for j in range(m)] for i in range(n)]

for i in range(n):
    if i%2==1:
        for j in range(m):
            if j%2==1:
                x[i][j]='#'
            if j%2==0:
                x[i][j]='*'
    elif i%2==0:
        for j in range(m):
            if j%2==1:
                x[i][j]='*'
            if j%2==0:
                x[i][j]='#'
                
for i in range(n):
    for j in range(m):     
        print(x[i][j],end=' ')
    print()