dict1={10:"Ganesh",11:"vijayawada",12:22}
print(dict1,type(dict1))
d1={}
print(d1,type(d1),id(d1))
print(len(d1))
d1[10]="RG"
d1[20]="AG"
d1[30]="PG"
print(d1,type(d1),id(d1))
#print(d1.clear())
#pop()
print(d1.pop(10))
print(d1)
#popitem
print(dict1.popitem())
print(dict1)
#get
dict2={"apple":25,"Guvava":95,"Orange":50}
print(dict2.get("apple"))
print(dict2.get("sw"))
#keys
print(dict2.keys())
d2=dict()
print(d2,type(d2))
print(d2.keys())
#values
print(dict2.values())
#items
print(dict2.items())
#copy(doubt)
d3={"India":1947,"china":1948,"USA":1774}
d4={"ABC":10,"DEF":20,"GHI":30}
d4=d3.copy()
print(d4)
print(d3)
#update
d5={"Name":"abc","age":25}
d6={"city":"HYD","NUM":99999}
d5.update(d6)
print(d5)
print(d6)