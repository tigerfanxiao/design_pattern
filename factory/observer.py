from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass


class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)  # 把生产者传给消费者


class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info  # 在类外面无法直接访问的私有成员

    @property
    def company_info(self):
        return self.__company_info  # 只有私有化这个company_info这个属性，才能做setter

    # 定义setter的目的时在修改company_info这个属性值是，我还需要做其他操作，比如更新所有订阅者
    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()  # 更新所有的观察者


class Staff(Observer):
    def __init__(self):
        self.company_info = None  # 观察者维护自己的信息

    def update(self, notice):
        self.company_info = notice.company_info


if __name__ == '__main__':
    staff1 = Staff()
    staff2 = Staff()
    notice = StaffNotice("初始公司信息")
    notice.attach(staff1)
    notice.attach(staff2)
    notice.company_info = "今年效益好，发奖金了"
    print(staff1.company_info)
    notice.company_info = "下班了"
    print(staff1.company_info)

    # 删除一个观察者
    notice.detach(staff1)
    notice.company_info = "删除了staff1"
    print(staff1.company_info)  # 被删除订阅之后，没有收到新的消息
    print(staff2.company_info)


