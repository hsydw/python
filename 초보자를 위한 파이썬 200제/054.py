class Mother:
    def sum(self, num1, num2):
        return num1+num2

class Son(Mother):
    def sub(self, num1, num2):
        return num1-num2

obj = Son()
print(obj.sum(5, 10))
print(obj.sub(7,3))
