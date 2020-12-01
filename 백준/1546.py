a = int(input())
b = list(map(int, input().split()))
high = max(b)
for i in range(a):
    b[i] = b[i]/high*100
    avg = sum(b)/a
print(avg)
