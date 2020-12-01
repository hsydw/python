class YonyClass:
    str = '안녕하세요.'
    def hi(self):
        param1 = 'hello'
        self.param2 = 'bye'
        print(param1)
        print(self.str)

obj = YonyClass()
print(obj.str)
obj.hi()

