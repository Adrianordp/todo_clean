"""Test use case for getting tasks."""

from todo_clean.layer0.entity.task import ITask, Task
from todo_clean.layer1.usecase.get_tasks import (
    GetTasks,
    GetTasksResponse,
    IGetTasksPresenter,
    IGetTasksRepository,
)


class RepositoryStub(IGetTasksRepository):
    """Spy for get tasks repository."""

    def __init__(self, fake_data: list[tuple[int, ITask]]):
        self.get_tasks_called = False
        self.fake_data = fake_data

    def get_tasks(self) -> list[tuple[int, ITask]]:
        self.get_tasks_called = True
        return self.fake_data

    def set_fake_data(self, fake_data: list[tuple[int, ITask]]) -> None:
        """Set fake data for repository."""
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
    fake_data = [(1, Task("Random ITask"))]
    repository_stub = RepositoryStub(fake_data)
    presenter_spy = PresenterSpy()

    response = GetTasksResponse(
        [(fake_data[0][0], fake_data[0][1].description)]
    )

    usecase = GetTasks(repository_stub, presenter_spy)
    usecase.execute()

    assert repository_stub.get_tasks_called is True

    assert presenter_spy.format_called is True
    assert presenter_spy.format_called_with["response"] == response
