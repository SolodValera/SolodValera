f=open('Солод Валерий Уб-51 vvod.txt')
n=int(f.readline())
matr=[]
for i in range(n):
    s=[int(i) for i in f.readline().split()]
    matr.append(s)
    
maxi=0
ans=[]
for i in range(n):
    for j in range(n):
        if abs(matr[i][j])>maxi:
            ans=i,j
            maxi=abs(matr[i][j])

del matr[ans[0]]
for i in matr:
    del i[ans[1]]
f.close()

qq=open('Солод Валерий Уб-51 vivod.txt','w')
for j in matr:
    stroka=' '.join([str(i)for i in j])
    qq.write(f'{stroka}\n')
qq.close()    
