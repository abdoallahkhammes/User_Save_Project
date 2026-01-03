from abc import ABCMeta, abstractmethod, ABC
from dataclasses import dataclass
from unittest.mock import Mock


class UserSavingRepositoryInterface(metaclass=ABCMeta):
    def __init__(self,User_Saving_Repository,presenter):
         self.presenter = presenter

    def execute(self, param):
      self.presenter.present(param)


class SavingUserUseCase:
    def execute(self, param):
        pass


class PresenterInterface(ABC):
    @abstractmethod
    def present(self, output_dto):
        pass

@dataclass
class OutputDTO:
    Name: str
    Email: str
    Phone: str


def test_should_save_user_successfully():
    #Arrange
    User_Saving_Repository = Mock(spec=UserSavingRepositoryInterface)
    presenter = Mock (spec=PresenterInterface)
    use_case = SavingUserUseCase(presenter)
    output_dto = OutputDTO(Name= None, Email= None, Phone= None)


    #act
    use_case.execute(None)

    #Assert
    presenter.present.assert_called_once_with(output_dto)