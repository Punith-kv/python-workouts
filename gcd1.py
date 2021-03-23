def Computegcd(a,b):
    if b==0:
        return a
    else:
        return Computegcd(b,a%b)
    
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
print(Computegcd(num1,num2))