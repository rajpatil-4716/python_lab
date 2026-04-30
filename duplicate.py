d = {"a":10, "b":20, "c":10, "d":30, "e":20}
k = {}

for x in d.values():
    k[x]=k.get(x,0)+1
for c,y in k.items():
        if y>1:
            print(x,":",y)

