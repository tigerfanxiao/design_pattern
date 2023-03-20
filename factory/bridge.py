from abc import ABCMeta, abstractmethod
# 有两个维度： 形状和颜色


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self, color):
        pass


class Color:
    @abstractmethod
    def paint(self, shape):
        pass


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)  # 注意： 这里把self传给了color

# 如果要增加一个形状
class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)



class Red(Color):
    name = "红色"

    def paint(self, shape):
        print(f"{self.name}的{shape.name}")


if __name__ == "__main__":
    red_circle = Circle(Red())
    red_circle.draw()

    red_rectangle = Rectangle(Red())
    red_rectangle.draw()