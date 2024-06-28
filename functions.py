#approch1
def cumm(a,b):
    c=a+b
    return c
res=cumm(10,20)
print("result is",res)

#approch2
def sumop():
    a=int(input("a"))
    b=int(input("b "))
    c=a+b
    print("sumops",c)
sumop()

#approch3
def sumop():
    a=int(input("a "))
    b=int(input("b "))
    c=a+b
    return("sum {} and {}={}".format(a,b,c))
result=sumop()
print(result)

#approch4
def sumop(a,b):
    c=a+b
    print("sum ({},{})={}".format(a,b,c))
a=int(input("a "))
b=int(input("b "))
sumop(a,b)

def sqrt(a):
    b=a**2
    return b
a=int(input("a"))
res=sqrt(a)
print("result is",res)

def sqrt():
    n=int(input("a "))
    a=n**2
    print("result is",a)
sqrt()



def sqrt():
    a=int(input("Enter a number: "))
    n=a**0.5
    return n
res=sqrt()
print("the result is",res)


def sqrt(a):
    b=a**2
    print("the square is",b)
a=int(input("a "))
sqrt(a)