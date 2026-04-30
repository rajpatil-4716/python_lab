d={101:"khushi", 899:"ridhi", 767:"ansh", 545:"shivani", 323:"zeel", 122:"chetanya"}

print(d)
print(d[323])
#print(d["zeel"])
print(d.get(101))
print(d.items())
print(d.keys())
print(d.pop(767))
print(d)
d.popitem()
print(d)
d1={767:"anshu", 122:"chetanya"}
d.update(d1)
print(d)
print(d.values())

for i in d:
    print(i,":",d[i])
    
for key,value in d.items():
    print(key,":",value)

if 899 in d:
    print("899 is in dictionary")
else:
    print("899 not in dictionary")
    
s=input("Enter String: ")
d={}

for i in s:
    d[i]=d.get(i,0)+1
    print(d)
    
n=int(input("Enter Number: "))
d={}

for i in range(1,n+1):
    d[i]=i*i
    print(d)

    
d={1:"jigar",2:"ajay",3:"vijay"}

key=int(input("Enter your key: "))
value=input("Enter new value: ")

if key in d:
    d[key]=value
else:
    print("key is not found")
print(d)    

