"""
Test use case for creating a task.
"""

from todo_clean.layer0.entity.task import ITask, Task
from todo_clean.layer1.usecase.create_task import (
    CreateTask,
    CreateTaskRequest,
    CreateTaskResponse,
    ICreateTaskPresenter,
    ICreateTaskRepository,
)


class RepositoryStub(ICreateTaskRepository):
    """
    Stub for creating task repository.
    """

    new_task_called = False
    new_task_called_with = {}

    def create_task(self, description: str) -> ITask:
        self.new_task_called = True
        self.new_task_called_with["description"] = description
        return Task(1, description)


class PresenterSpy(ICreateTaskPresenter):
    """
    Spy for creating task presenter.
    """

    format_called = False
    format_called_with = {}

    def format(self, response: CreateTaskResponse) -> None:
        self.format_called = True
        self.format_called_with["response"] = response


def test_usecase_create_new_task():
    """
    Test use case for creating a new task.
    """
    description = "Random ITask"

    request = CreateTaskRequest(description)
    repository_stub = RepositoryStub()
    presenter_spy = PresenterSpy()

    usecase = CreateTask(repository_stub, presenter_spy)
    usecase.execute(request)

    assert repository_stub.new_task_called is True
    assert repository_stub.new_task_called_with["description"] == description

    assert presenter_spy.format_called is True
    assert presenter_spy.format_called_with["response"] == CreateTaskResponse(
        1, description
    )
