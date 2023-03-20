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


# 抽象工厂角色
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


# 具体工厂，为每一个类创建一个工厂
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


if __name__ == "__main__":
    alipay_factory = AlipayFactory()
    alipay = alipay_factory.create_payment()
    alipay.pay()