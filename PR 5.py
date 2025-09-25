
#ПР 5
#9
'''
lst='Привет, меня зовут Валера, я учусь на 1 курсе во ВГУИТ. Привет, а меня зовут Толян, я тоже там учусь'
lst=lst.split()
n=input()
a=lst.count(n)
print(a)
'''
#14
a=input()
a=a.split()
lst=[]
for i in a:
    print(i)
    if (i[0]=='а') and (i[-1]=='я'):
        lst.append(i)
print(lst)