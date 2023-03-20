from abc import ABCMeta, abstractmethod


class Player:
    def __int__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGilrBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()  # 这里先建立了一个空对象，这就要求建立对象时，要赋予默认值

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条身材"

    def build_arm(self):
        self.player.arm = "漂亮胳膊"

    def build_leg(self):
        self.player.leg = "大长腿"

    
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()  # 这里先建立了一个空对象，这就要求建立对象时，要赋予默认值

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "长毛的胳膊"

    def build_leg(self):
        self.player.leg = "长毛的腿"


# 控制组装顺序
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# 客户端
builder = SexyGilrBuilder()
director = PlayerDirector()
player1 = director.build_player(builder)
print(player1)
