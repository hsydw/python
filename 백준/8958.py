n = int(input())
for i in range(n):
    num1 = input()
    score = 0
    count = 0
    for j in range(len(num1)):
        if num1[j] == 'O':
            count += 1
            score += count
        else:
            score += 0
            count = 0
    print(score)
