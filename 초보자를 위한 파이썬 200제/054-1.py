class Mother:
    def sum(self, num1, num2):
        return num1+num2

class Father:
    def mul(self, num1, num2):
        return num1*num2
    
class Son(Mother,Father):
    def sub(self, num1, num2):
        return num1-num2

obj = Son()
print(obj.sum(5, 10))
print(obj.sub(7,3))
print(obj.mul(2,3))
