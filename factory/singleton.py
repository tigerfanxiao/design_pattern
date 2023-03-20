
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):  # 如果类被继承，这里的cls是子类
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# 定义一个类， 这个类是一个单例模式
class MyClass1(Singleton):
    def __init__(self, a):
        self.a = a


class MyClass2(Singleton):
    def __init__(self, c):
        self.c = c


if __name__ == '__main__':
    a = MyClass1(10)
    b = MyClass1(20)
    print(a.a, b.a)  # 20， 20
    print(id(a), id(b))  # 同一个对象

    c = MyClass2('fanxiao')
    print(c.c)

    print(a.a)