# 简单工厂方法
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print(f'Alipay {money}')


class WechatPay(Payment):
    def pay(self, money):
        print(f'Wechatpay {money}')


# 用一个工厂方法来初始化
def create_payment(method):
    if method == 'alipay':
        return Alipay()
    if method == 'wechatpay':
        return WechatPay()
    raise TypeError(f"No such payment method {method}")


if __name__ == "__main__":
    # 客户端代码不知道对象是怎么创建的
    alipay = create_payment("alipay")
    alipay.pay(50)
    