# Files: 
# Author：jiang liu
# Date ：2020/3/25 20:50
# Tool ：PyCharm


class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calaulate(self):
        print('算你个123456')
        print("cpu对象：", self)


class Screen:
    def show(self):
        print('亮瞎你的狗眼')
        print("screen对象：", self)


m = MobilePhone(CPU(), Screen())

m.cpu.calaulate()
m.screen.show()
