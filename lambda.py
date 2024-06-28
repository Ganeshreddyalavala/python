#lambda function
"""def findbig(a,b,c):
    if(a>b) and (a>c):
        return a
    if(b>c) and (b>a):
        return b
    if(c>a) and(c>b):
        return c

big= lambda a,b,c: (a if (a > b and a > c) else b if b > c else c)                


a=int(input("Enter a"))
b=int(input("enter b"))
c=int(input("Enter c"))
result=findbig(a,b,c)
print("findbig ({},{},{})={}".format(a,b,c,result))"""

#lambda function 2
div=lambda a,b: a%b==0
a=int(input('ENTER THE VALUE OF A'))
b=int(input("Enter the value of b"))
divi=div(a,b)
print("the result is perfect division",divi)
