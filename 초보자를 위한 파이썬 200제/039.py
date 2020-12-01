def sum1(num1, num2):
    ret = num1+num2
    return ret

def txt1(text1, text2):
    ret = text1+text2
    return ret

def txt2(text3, text4):
    print(text3+text4)

text3 = '나는'
text4 = '김철수'

answer1 = sum1(10, 20)
print(answer1)

answer2 = txt1('안녕', '하세요')
print(answer2)

txt2(text3,text4)
