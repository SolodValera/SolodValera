#9/.1
'''
k=int(input('кратен'))
n=int(input())
ar=[]
for i in range(n):
    ar.append([int(i)for i in input().split()])

maxi=-1000
for i in range(n):
    for j in range(n):
        if (ar[i][j]%k==0) and (ar[i][j]>maxi):
            maxi=ar[i][j]
        
for i in ar:
    print(*i)
print(maxi)
'''
#9/2
'''
n=int(input())
matr=[]
for i in range(n):
    s=[int(i) for i in input().split()]
    matr.append(s)

maxi=-9161
ans=0
for i in range(n):
    for j in range(n):
        if abs(matr[i][j])> maxi:
            maxi=abs(matr[i][j])
            ans=(i,j)
     
del matr[ans[0]]
for i in matr:
    del i[ans[1]]
print(maxi,ans)

for i in matr:
    print(*i)
