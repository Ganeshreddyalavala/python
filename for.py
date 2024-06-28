"""n=9
for i in range(1,11):
    print("{}*{}={}".format(n))
    print(n*i)

a=int(input("Enter the number"))
for i in range(1,11):
    print("{}*{}={}".format(a,i,a*i))"""
"""s=0
n=input("Enter a number")
for i in n:
    x=int(i)
    print("type of i={} and x={}".format(type(i),type(x)))
    s=s+x
else:
    print("sum({})={}".format(n,s))"""
"""n=int(input("Enter a value"))
l1=list()
for i in range(1,n+1):
    val=float(input("Enter the value {}".format(i)))
    l1.append(val)
else:
    print("content of list={}".format(l1))
    print("sum={}".format(l1))
    print("Avg={}".format(sum(l1)/len(l1)))"""

#BREAK
"""n=int(input("Enter the number"))
result="PRIME"
for i in range(2,n):
    if n%i==0:
        result="NOT PRIME"
        break
if(result=="PRIME"):
    print("its  prime number")
else:
    print("its not a prime")"""

#continue
s="PYTHON"
for val in s:
    if(val=="T"):
        continue
    print("\t{}".format(val))
else:
    print("\n I am from else part")

s="PYTHON"
for val in s:
    if(val=="T") or (val=="H"):
        continue
    print("\t{}".format(val))
else:
    print("\n I am from else part")

