


class CPU:
    def run(self):
        print(f"CPU run")

    def stop(self):
        print("CPU stop")


class Memory:
    def run(self):
        print("Memory run")

    def stop(self):
        print("Memory stop")

class Disk:
    def run(self):
        print("Disk run")
    def stop(self):
        print("Disk Stop")


class Computer:
    def __init__(self):
        self.cpu = CPU()  # 注意：这里的初始化没有传入参数，也就说没有让client段来控制
        self.memory = Memory()
        self.disk = Disk()

    def run(self):
        self.cpu.run()
        self.memory.run()
        self.disk.run()

    def stop(self):
        self.cpu.stop()
        self.memory.stop()
        self.disk.stop()


if __name__ == '__main__':
    computer = Computer()  # 对于客户端而言，没有控制cpu，memory，stop的接口。只有控制computer的接口
    computer.run()