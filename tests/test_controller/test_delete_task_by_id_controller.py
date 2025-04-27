"""
Test controller for deleting a task.
"""

from todo_clean.layer1 import (
    DeleteTaskByIdRequest,
    DeleteTaskByIdResponse,
    IDeleteTaskById,
    IDeleteTaskByIdPresenter,
    IDeleteTaskByIdRepository,
)
from todo_clean.layer2 import DeleteTaskByIdController


class RepositoryDummy(IDeleteTaskByIdRepository):
    """
    Dummy for deleting task repository.
    """

    def delete_task_by_id(self, _: int) -> bool:
        pass


class UseCaseSpy(IDeleteTaskById):
    """
    Spy for deleting task use case.

    :param IDeleteTaskByIdRepository task_repo: The repository for deleting a task.
    :param IDeleteTaskByIdPresenter presenter: The presenter for deleting a task.
    """

    execute_called = False
    execute_called_with = {}

    def __init__(
        self, _: IDeleteTaskByIdRepository, __: IDeleteTaskByIdPresenter
    ):
        pass

    def execute(self, request: DeleteTaskByIdRequest) -> None:
        self.execute_called = True
        self.execute_called_with["request"] = request


class PresenterDummy(IDeleteTaskByIdPresenter):
    """Dummy for deleting task presenter."""

    def format(self, _: DeleteTaskByIdResponse) -> None:
        pass


def test_controller_delete_task_by_id():
    """Test controller for deleting a task."""
    id_ = 1
    task_repo_stub = RepositoryDummy()
    presenter_dummy = PresenterDummy()

    usecase_spy = UseCaseSpy(task_repo_stub, presenter_dummy)
    controller = DeleteTaskByIdController(usecase_spy)
    controller.handle(id_)

    assert usecase_spy.execute_called is True
    assert isinstance(
        usecase_spy.execute_called_with["request"], DeleteTaskByIdRequest
    )
    assert usecase_spy.execute_called_with["request"].id_ == 1
