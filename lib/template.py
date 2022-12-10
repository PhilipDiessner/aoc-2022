from abc import ABC, abstractmethod


class Solution(ABC):
    def __init__(self, path) -> None:
        self.data = self.get_input(path)
        super().__init__()


    @abstractmethod
    def get_input(self, path):
        pass

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass
