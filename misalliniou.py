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

"""s="PYTHON"
for val in s:
    if(val=="T") or (val=="H"):
        continue
    print("\t{}".format(val))
else:
    print("\n I am from else part")"""

n=int(input("enter the number"))
lst=list()
for i in range(1,n+1):
    val=float(input("enter {} value:".format(i)))
    lst.append(val)
else:
    print("content of the list = {}".format(lst))
    pslist=[]
    for val in lst:
        if val<=0:
               continue
        pslist.append(val)
