thist = {"apple", "banana", "cherry"}
print(thist)

for x in thist:
    print(x)

print(len(thist))


thist_list = list(thist)
thist_list[0] = "hello"
print(thist_list)
