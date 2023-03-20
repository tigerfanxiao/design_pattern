# 这里展示了 NotImplementedError的用法

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError  # 注意报错的位置是定义在抽象类里


class WechatPay(Payment):
    def pay(self, money):
        pass


class Alipay(Payment):
    pass


if __name__ == '__main__':
    wechatpay = WechatPay()
    wechatpay.pay(100)  # 方法被实现，不会报错

    alipay = Alipay()  # 在创建对象的时候不会报错
    alipay.pay(899)  # 在使用方法的时候，因为方法没有被实现，所以会报错


