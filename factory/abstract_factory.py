from abc import ABCMeta, abstractmethod


class Shell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class AppleShell(Shell):
    def show_shell(self):
        print("苹果手机壳")


class MiShell(Shell):
    def show_shell(self):
        print("小米手机壳")


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("晓龙CPU")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("安卓OS")


class IOS(OS):
    def show_os(self):
        print("苹果IOS")


class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

    @abstractmethod
    def make_shell(self):
        pass


class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()  # 这里控制了每一种手机只能选择固定的cpu类型

    def make_os(self):
        return Android()

    def make_shell(self):
        return MiShell()


class IphoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


# 客户端

class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


if __name__ == '__main__':
    phone1 = make_phone(MiFactory())
    phone1.show_info()