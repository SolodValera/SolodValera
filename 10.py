
f=open('Солод Валерий Уб-51 vvod.txt')

k=int(f.readline())
n=int(f.readline())
matr=[]
for i in range(n):
    s=[int(i)for i in f.readline().split()]
    matr.append(s)

cnt=0
maxi=0
for i in range(n):
    for j in range(n):
        if matr[i][j]%k==0:
            cnt+=1
            if matr[i][j]>maxi:
                maxi=matr[i][j]
f.close()

qq=open('Солод Валерий Уб-51 vivod.txt','w')
qq.write(f'{cnt} {maxi}')


qq.close()













            




