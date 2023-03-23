from abc import ABC, abstractmethod


class BaseProducerEngine(ABC):
    """Класс абстрактного продюсера"""

    @abstractmethod
    def send(self, *args):
        """Абстрактный метод отправки события в указанный топик"""
        pass
