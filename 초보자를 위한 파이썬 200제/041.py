str1 = '이건 전역변수다.'
num1 = 5

def local1():
    str1 = '이건 지역변수다.'
    print(str1)

def func1(num1):
    num1 = 10
    

def func2():
    global num1
    num1 = 20
    global str1
    str1 = '메롱'
    
    
local1()

print(str1)
print(num1)

func1(num1)
print(num1)

func2()
print(num1)
print(str1)
