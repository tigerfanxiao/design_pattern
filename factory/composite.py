from abc import ABCMeta, abstractmethod
from typing import Iterable


class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self) -> None:
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"点({self.x}, {self.y})"

    def draw(self) -> None:
        print(str(self))


class Line(Graphic):
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"线段({self.p1}, {self.p2})"

    def draw(self) -> None:
        print(str(self))


# 组合
class Picture(Graphic):
    def __init__(self, iterable: Iterable[Graphic]):  # 初始化的时候就接收要给列表
        self.children = []
        for e in iterable:
            self.children.append(e)

    def add(self, graphic:Graphic) -> None:  # 这个方法是为了给初始化之后的组合添加元素的
        self.children.append(graphic)

    def draw(self) -> None:
        for e in self.children:
            e.draw()    # 这里有递归调用


if __name__ == '__main__':
    p1 = Point(2, 3)
    line1 = Line(Point(3, 4), Point(6, 7))
    line2 = Line(Point(1, 5), Point(2, 8))
    pic1 = Picture([p1, line1, line2])

    # pic1.draw()

    p2 = Point(4, 4)
    line3 = Line(Point(1, 1), Point(0, 0))

    pic2 = Picture([p2, line3])

    pic3 = Picture([pic1, pic2])
    pic3.draw()
