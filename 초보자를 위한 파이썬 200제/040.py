def txt3(text1, text2='축구선수'):
    print(text1 + '은(는) ' + text2)

txt3('구자철')
txt3(text1='이승엽', text2='야구선수')

def func1(*n):
    print(n)

func1()
func1(1,2,3)
func1('a', 'b')

def func2(a, b, **c):
    print(c)

func2(1, 2)
func2(1, 2, age=20, sex='male')
