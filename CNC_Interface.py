from abc import ABC, abstractmethod

class CNCInterface(ABC):
    @abstractmethod
    def calculate_stroke_1(self, stroke):
        pass
    @abstractmethod
    def calculate_stroke_2(self, stroke):
        pass   