"""Game extension that adds a bard character"""

from dataclasses import dataclass
from game import factory

@dataclass
class Bard:
    name: str
    instrument: str

    def make_a_noise(self) -> None:
        print(f"play {self.instrument}, Toss a coin to your Witcher")



# TODO: 不清楚这个函数是干嘛用的？
def initialize() -> None:
    factory.register("bard", Bard)