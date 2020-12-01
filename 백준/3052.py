list1 = []
for i in range(10):
    a = int(input())
    list1.append(a%42)
list1 = set(list1)
print(len(list1))
