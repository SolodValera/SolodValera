
'''
#3
a=int(input())
b=int(input())
for i in range(a,b-1,-1):
    if i%2!=0:
         print(i)
'''
#9
'''
n=int(input())
a=0
b=1
summa=0
for i in range(n):
    summa+=a
    peremenaya=a
    a=b
    b=peremenaya+b
print(summa)
'''
#4
'''
n=int(input())
summa=0
for i in range(n):
    summa+=int(input())
print(summa)
'''

