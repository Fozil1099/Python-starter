import math 
a=float(input("sonni kiriting: "))
n=int(input("darajani kiriting: "))
s=0
r=1

for i in range(1, n+1):
    s+=r*(math.pow(a,i))
    r*=-1
    print(s)
print(a," ning ",n," darajasi yegindilari: ", s)
    
