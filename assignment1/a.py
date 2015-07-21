from collections import Counter

a=[1,2,2,3,3,4,3]
a.append(4)
b=Counter(a)

for k,v in b.most_common():
    print(str(k)+"="+str(v))

