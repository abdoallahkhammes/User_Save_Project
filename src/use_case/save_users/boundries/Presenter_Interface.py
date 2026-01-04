from abc import ABC, abstractmethod


class PresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto):
        pass
