from unittest.mock import Mock

from src.use_case.save_users.boundries.Presenter_Interface import PresenterInterface
from src.use_case.save_users.dependencies.User_Saving_Repository_Interface import UserSavingRepositoryInterface
from src.use_case.save_users.output_dto import OutputDTO
from src.use_case.save_users.use_case import SavingUserUseCase


def test_should_save_user_successfully():
    # Arrange
    User_Saving_Repository = Mock(spec=UserSavingRepositoryInterface)
    presenter = Mock(spec=PresenterInterface)
    use_case = SavingUserUseCase(User_Saving_Repository, presenter)

    # Debug: انظر ماذا يحدث
    def print_call(arg):
        print(f"presenter.present called with: {arg}")
        print(f"Type: {type(arg)}")

    presenter.present.side_effect = print_call

    output_dto = OutputDTO(Name=None, Email=None, Phone=None)

    # Act
    use_case.execute(output_dto)

    # Assert
    # سترى في output ماذا يتم تمريره فعلاً