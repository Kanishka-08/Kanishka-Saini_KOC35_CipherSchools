import random
def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

a=int(input("Enter the Lower limit: "))
b=int(input("Enter the Upper limit: "))
x=random.randint(a,b)
print("\n")
print("Range is (%d) and randomly picked number is %d"%(b-a,x))
if(x>0):
    print("%d is an 'Positive' number"%(x))
else:
    print("%d is an 'Negative' number"%x)
if(x%2==0):
    print("%d is an 'Even' number"%(x))
else:
    print("%d is an 'Odd' number"%x)
if(x==1):
    print("1 is neither pime nor composite number")
elif(prime(x)):
    print("%d is a 'Prime' number"%x)
else:
    print("%d is a 'Composite' number"%x)
    







