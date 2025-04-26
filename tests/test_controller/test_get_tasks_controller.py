"""
Test controller for getting tasks.
"""

from todo_clean.layer0.entity.task import ITask
from todo_clean.layer1.usecase.get_tasks import (
    GetTasksResponse,
    IGetTasks,
    IGetTasksPresenter,
    IGetTasksRepository,
)
from todo_clean.layer2.controller.get_tasks_controller import (
    GetTasksController,
)


class RepositoryDummy(IGetTasksRepository):
    """
    Dummy repository for testing.
    """

    def get_tasks(self) -> list[ITask]:
        pass


class PresenterDummy(IGetTasksPresenter):
    """
    Dummy presenter for testing.
    """

    def format(self, _: GetTasksResponse) -> None:
        pass


class UseCaseSpy(IGetTasks):
    """
    Spy for creating task use case.
    """

    execute_called = False

    def __init__(self, _: IGetTasksRepository, __: IGetTasksPresenter):
        pass

    def execute(self) -> None:
        self.execute_called = True


def test_get_tasks_controller():
    """
    Test controller for getting tasks.
    """
    repository_dummy = RepositoryDummy()
    presenter_dummy = PresenterDummy()
    usecase_spy = UseCaseSpy(repository_dummy, presenter_dummy)

    controller = GetTasksController(usecase_spy)

    controller.handle()

    assert usecase_spy.execute_called is True
