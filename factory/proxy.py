from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self):
        pass


class RealSubject(Subject):

    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):
    # 如果文件很大，在创建文件对象的时候， 不用读取内容
    # 复用之前realsubject类
    def __init__(self, filename):
        self.filename = filename
        self.subject = None  # 这里应该处理一个对象，而不再是直接处理文字

    def get_content(self):
        if not self.subject:
            self.subject = RealSubject(filename=self.filename)
        return self.subject.get_content()

    def set_content(self, content):
        if not self.subject:
            self.subject = RealSubject(filename=self.filename)
        self.subject.set_content(content)


class ProtectProxy(Subject):
    def __init__(self, filename):
        self.subject = RealSubject(filename=filename)

    def get_content(self):
        return self.subject.get_content()

    def set_content(self):
        raise PermissionError("No previlege, need to login")

