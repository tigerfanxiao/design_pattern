from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# 一个公司的代码
class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d" % money)


# 另一个公司的代码, 这个类已经被其他类使用了，不清轻易修改
# 现在要是这个类适应Alipay的写法
class WechatPay:
    def cost(self, money):
        print("微信支付%d" % money)


class BankPay:
    def cost(self, money):
        print("银联支付%d" % money)


# 写类适配器
class WechatPayAdapter(Payment, WechatPay):
    def pay(self, money):
        WechatPay().cost(money)

# 如果有很多类都需要做适配，则可以做一个对象适配器来
class PaymentAdapter(Payment):
    def __init__(self, new_payment):
        self.payment = new_payment

    def pay(self, money):
        return self.payment.cost(money)



if __name__ == '__main__':
    wechat_pay = WechatPayAdapter()
    wechat_pay.pay(100)

    bank_pay = PaymentAdapter(BankPay())
    bank_pay.pay(200)