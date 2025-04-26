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

    def __init__(self, fake_task: ITask = Task(1, "Random ITask")):
        self.new_task_called = False
        self.new_task_called_with = {}
        self.fake_task = fake_task

    def create_task(self, description: str) -> ITask:
        self.new_task_called = True
        self.new_task_called_with["description"] = description
        return self.fake_task


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
    description = "Random Task"
    id_ = 2
    task = Task(id_, description)

    request = CreateTaskRequest(description)
    repository_stub = RepositoryStub(task)
    presenter_spy = PresenterSpy()

    usecase = CreateTask(repository_stub, presenter_spy)
    usecase.execute(request)

    assert repository_stub.new_task_called is True
    assert repository_stub.new_task_called_with["description"] == description

    assert presenter_spy.format_called is True
    assert isinstance(
        presenter_spy.format_called_with["response"], CreateTaskResponse
    )
    assert presenter_spy.format_called_with["response"].id_ == id_
    assert (
        presenter_spy.format_called_with["response"].description == description
    )
    assert presenter_spy.format_called_with["response"] == CreateTaskResponse(
        id_, description
    )

    assert usecase.get_presenter() == presenter_spy
