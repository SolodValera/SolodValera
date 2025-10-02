
#12.1
'''
lst=[5,4,6,4,2,3,8]
lst1=[]
for i in lst:
    if i%2!=0:
        lst1.append(i)
print(min(lst1))#минимальное нечетное 
'''
#12.2
'''
A=[5,5,5,5,5,6,6,6,6,6]
B=[1,1,1,1,1,9,9,9,9,9]
lst1=A
lst2=B
A=lst2
B=lst1
print(A,B)
'''

#9.1
n=int(input('сколько элементов'))
lst=[]
for i in range(n):
    a=float(input('введите массив'))
    lst.append(a)
mini=1000000 #минимальрный элемент
for i in range(len(lst)):
    m=abs(lst[i])
    if m<mini:
        mini=m
print(mini)#минимальный по модулю элемент




#9.2
'''
A=[5,5,5,5,5,6,6,6,6,6]
B=[1,1,1,1,1,9,9,9,9,9]
print(A,B)
lst1=A
lst2=B
A=lst2
B=lst1
print(A,B)
'''
