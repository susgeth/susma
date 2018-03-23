n=0
a=[]
num1=int(input("Enter the array size:"))
num2=int(input("How many first n digits u want to add?"))
print("Enter number  in sequence")
for n in range(0,num1):
    y=int(input())
    a.append(y)
b=0
for n in range(0,num2):
    b+=a[n]
print(b)
