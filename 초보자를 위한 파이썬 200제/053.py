class YonyClass():
    def __del__(self):
        print('인스턴스 객체를 메모리에서 제거했습니다.')

obj = YonyClass()
del obj
