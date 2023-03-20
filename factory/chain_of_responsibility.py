from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print(f"经理准假{day}天")
        else:
            print(f"你还是辞职吧")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print(f"部门主管准假{day}天")
        else:
            print("部门主管权限不足")
            self.next.handle_leave(day)


class ProjectDirecter(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print(f"项目主管准假{day}天")
        else:
            print(f"项目主管权限不足")
            self.next.handle_leave(day)


if __name__ == '__main__':
    day = 11
    manager = ProjectDirecter()
    manager.handle_leave(day)