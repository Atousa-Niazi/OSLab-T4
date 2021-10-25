#Atousa-Niazi-Abkoh-98440127-Python-Fibonacci-OSLab-T4.4

print('enter n:')
n=int(input())
f= [0 for j in range(n+1)]
f[0]=0
f[1]=1
for i in range(2,n+1):
    f[i]=f[i-1]+ f[i-2]

print(f)