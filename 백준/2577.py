a = int(input())
b = int(input())
c = int(input())
res = list(str(a*b*c))
for i in range(10):
    print(res.count(str(i)))
