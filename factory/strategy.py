from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print(f"用较快的方式处理数据")


class SlowStrategy(Strategy):
    def execute(self, data):
        print(f"用较慢的方式处理数据")


class Context:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy):  # 做策略切换
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(data=self.data)


if __name__ == '__main__':
    strategy = FastStrategy()
    data = 'fanxiao'
    context = Context(strategy, data)
    context.set_strategy(SlowStrategy())
    context.do_strategy()