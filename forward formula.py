import numpy as np, tabulate
from numpy.lib.function_base import append
Data=[];data=[];heading=[]
n=int(input("Number of data points: "))
x=np.zeros(n)
y=np.zeros((n,n))

print("Enter x values")
for i in range(n):
    x[i]=eval(input('x['+str(i)+']= '))

heading.append('x')
heading.append('y')

print("Enter y values")
for i in range(n):
    y[i][0]=eval(input('y['+str(i)+']= '))
    heading.append('Δ'+str(i+1)+'y')

for i in range(1,n):
    for j in range(0,n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]



print("Table:")
""" 
for i in range(0,n):
    print('%0.4f' %(x[i]), end='')
    for j in range(0, n-i):
        print('   %0.4f' %(y[i][j]), end='')
    print()
"""

for i in range(0,n):
    data.append(x[i])
    for j in range(0, n-i):
        data.append(y[i][j])
    c=data.copy()
    data.clear()
    Data.append(c)
print(tabulate.tabulate(Data,heading,tablefmt='fancy_grid'))

#interpolation formula (forward)

a=float(input("Enter the value to interpolate: "))
u=(a-x[0])/(x[1]-x[0])

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def u_call(u,n):
    temp=u
    for i in range(1,n):
        temp*=(u-i)
    return temp

sum=y[0][0]
for i in range(1,n):
    sum=sum+(u_call(u,i)*y[0][i])/fact(i)

print("The sum is ",sum)
