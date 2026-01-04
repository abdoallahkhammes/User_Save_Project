from abc import ABCMeta, abstractmethod


class UserSavingRepositoryUseCaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, param):
        pass
