thist = ("apple","banana","cherry")

print(thist)

for x in thist:
    print(x)
    
print(len(thist))

for x in range(0,len(thist)):
    print(x," ")
    print(thist[x])

for x in thist:
    print(x)
    
print(len(thist))

for x in range(0,len(thist)):
    print(x," ")
    print(thist[x])
    
    thist[0]="hello"
    print(thist)
