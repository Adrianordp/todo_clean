"""
Test use case for getting tasks.
"""

from todo_clean.layer0.entity.task import ITask, Task
from todo_clean.layer1.usecase.get_tasks import (
    GetTasks,
    GetTasksResponse,
    IGetTasksPresenter,
    IGetTasksRepository,
)


class RepositoryStub(IGetTasksRepository):
    """
    Stub for get tasks repository.

    :param list[tuple[int, ITask]] fake_data: Fake data for stub repository.
    """

    def __init__(self, fake_data: list[tuple[int, ITask]]):
        self.get_tasks_called = False
        self.fake_data = fake_data

    def get_tasks(self) -> list[tuple[int, ITask]]:
        """
        Get fake tasks from stub repository.

        :return list[tuple[int, ITask]]: The list of fake tasks.
        """
        self.get_tasks_called = True
        return self.fake_data

    def set_fake_data(self, fake_data: list[tuple[int, ITask]]) -> None:
        """
        Set fake data for repository.
        """
        self.fake_data = fake_data


class PresenterSpy(IGetTasksPresenter):
    """Spy for get tasks presenter."""

    format_called = False
    format_called_with = {}

    def format(self, response: GetTasksResponse):
        self.format_called = True
        self.format_called_with["response"] = response


def test_usecase_get_tasks():
    """Test use case for getting tasks."""
    fake_data = [Task(1, "Random ITask")]
    repository_stub = RepositoryStub(fake_data)
    presenter_spy = PresenterSpy()

    response = GetTasksResponse([(fake_data[0].id_, fake_data[0].description)])

    usecase = GetTasks(repository_stub, presenter_spy)
    usecase.execute()

    assert repository_stub.get_tasks_called is True

    assert presenter_spy.format_called is True
    assert presenter_spy.format_called_with["response"] == response

    assert usecase.get_presenter() == presenter_spy
