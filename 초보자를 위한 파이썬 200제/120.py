list1 = ['민수','철주','영희','길동','천식']
res1 = list(enumerate(list1))
print(res1)

for i, name in enumerate(list1):
    print('기호 %d번 %s' %(i+1,name))
