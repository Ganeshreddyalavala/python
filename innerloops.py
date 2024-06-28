"""for i in range(1,6):
    for j in range(1,4):
        print(j)
print(i)"""

"""i=1
while(i<6):
 print("Val of i (outer Loop)=",i)
 print("-------------------------------------")
 j=1
 while(j<4):
     print("Val of j (Inner Loop)=",j)
     j=j+1
 else:
     print("I am out of inner loop")
     i=i+1
 print("-------------------------------------")
else:
 print("i am out of outer loop")"""

"""i=1
while i<6:
    print(i)
    j=1
    while j<4:
        print(j)
        j=j+1
    else:
        i=i+1

for i in range(5,0,-1):
    print(i)
    j=3
    while j>0:
        print(j)
        j=j-1

i=1
while(i<6):
    print(i)
    i=i+1
    for j in range(3,0,-1):
        print(j)


lst=[10,20,5,18,45]
for n in lst:
    print(n)
    for j in range(1,11):
        print(n,j,n*j)"""

n=int(input("Enter How Many Values u have:"))
if(n<=0):
    print("{} is invalid input:".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=int(input("Enter {} value:".format(i)))
        lst.append(val)
    else:
     print("Content of List=",lst) # [1, 14, 12, 13, 17]
     pnlst=[]
     i=0
     while(i<len(lst)):
         n=lst[i]
     if(n<=1):
         print("{} is invalid Input:".format(n))
     else:
             result="Prime"
             for j in range(2,n):
                 if(n%j==0):
                     result="Not Prime"
                 break
                 if(result=="Prime"):
                     pnlst.append(n)
                     i=i+1
                 else:
                         print("Prime Numbers List={}".format(pnlst))