# Files: 
# Author：jiang liu
# Date ：2020/3/26 9:30
# Tool ：PyCharm


class CarFactory:

    def createCar(self, brand):
        if brand == '奔驰':
            print('奔驰')
            return Benz()
        elif brand == '宝马':
            print('宝马')
            return BMW()
        elif brand == '比亚迪':
            print('比亚迪')
            return BYD()
        else:
            return "未知品牌，无法创建"


class Benz:
    pass


class BMW:
    pass


class BYD:
    pass


factory = CarFactory()
# c1 = Benz()
# c2 = BMW()
# c3 = BYD()
c1 = factory.createCar("奔驰")
c2 = factory.createCar("宝马")
c3 = factory.createCar("比亚迪")
