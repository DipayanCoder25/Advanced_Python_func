numbers=[1,2,3,4,5,6,7,8]
even_numbers=[x for x in numbers if x%2==0]
print("Even number from the list are : ",even_numbers)
sqaure=[x**2 for x in range(10)]
print(sqaure)
num=[23,4,5,3,43,4,4,434]
list1=['Even ' if x%2==0 else 'Odd' for x in num ]
print(list1)
myDict={str(x):x**2 for x in[1,2,3,4,5]}
print(myDict)

nums=[2,1,3,4,5,6]
def sq(n):
    return n*n
l=list(map(sq,nums))
print("Square numbers : ",l)
print()
num1=[1,2,3]
num2=[4,5,6]
ev=map(lambda x,y:x+y ,num1,num2)
print(list(ev))

s1={2,3,1}
s2={'a','b','c'}
s3=list(zip(s1,s2))
print(s3)

key=['Dip','Aryan','Ben']
ar=['Bd','BD2','Aus']
print(list(zip(key,ar)))

for i in range(10):
    if i==5:
        print(exit)
        exit()
    else:
        print(i)
           