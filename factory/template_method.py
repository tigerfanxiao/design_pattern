from abc import ABCMeta, abstractmethod
from time import sleep


class Window(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # 只有这个方法是具体的，定义了程序的框架，有点类似WSGI
    # 高层程序负责实现原子操作
    def run(self):
        self.start()
        while True:
            try:
                sleep(1)
                self.repaint()
            except KeyboardInterrupt as e:
                break
        self.stop()


class MyWindow(Window):

    def start(self):
        print("Window starts")

    def stop(self):
        print("Window stopped")

    def repaint(self):
        print("Window repaint")



if __name__ == "__main__":
    window = MyWindow()
    window.run()