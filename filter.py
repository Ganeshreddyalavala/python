def positive(n):
    if(n>0):
        return True
    else:
        return False
def negative(n):
    if(n<0):
        return True
    else:
        return False
lst=[10,20,30,-12,-15]
filobj=filter(positive,lst)
plst=list(filobj)
print("positive numbers is",plst)
filobj1=filter(negative,lst)
neglist=list(filobj1)
print("negative numbers is",neglist)

psops=lambda a: a>0
ngops=lambda a: a<0
list1=[10,20,30,-15,-13,-6]
filobj=filter(psops,list1)
pslist=list(filobj)
print("positive element",pslist)
filobj1=filter(ngops,list1)
nglist=list(filobj1)
print("neg ele",nglist)

list1=[10,20,30,-15,-13,-6]
filobj=list(filter(lambda a: a>0,list1))
print("positive element",filobj)
filobj1=list(filter(lambda a: a<0,list1))
print("neg ele",filobj1)
