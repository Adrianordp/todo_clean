"""
Test controller for creating a task.
"""

from todo_clean.layer0.entity.task import ITask
from todo_clean.layer1.usecase.create_task import (
    CreateTaskRequest,
    CreateTaskResponse,
    ICreateTask,
    ICreateTaskPresenter,
    ICreateTaskRepository,
)
from todo_clean.layer2.controller.create_task_controller import (
    CreateTaskController,
)


class RepositoryDummy(ICreateTaskRepository):
    """
    Dummy for creating task repository.
    """

    def create_task(self, description: str) -> ITask:
        pass


class UseCaseSpy(ICreateTask):
    """
    Spy for creating task use case.

    :param ICreateTaskRepository task_repo: The repository for creating a task.
    :param ICreateTaskPresenter presenter: The presenter for creating a task.
    """

    execute_called = False
    execute_called_with = {}

    def __init__(self, _: ICreateTaskRepository, __: ICreateTaskPresenter):
        pass

    def execute(self, request: CreateTaskRequest) -> None:
        self.execute_called = True
        self.execute_called_with["request"] = request


class PresenterDummy(ICreateTaskPresenter):
    """Dummy for creating task presenter."""

    def format(self, response: CreateTaskResponse) -> None:
        pass


def test_controller_create_task():
    """Test controller for creating a task."""
    description = "Random task description"
    task_repo_stub = RepositoryDummy()
    presenter_dummy = PresenterDummy()

    usecase_spy = UseCaseSpy(task_repo_stub, presenter_dummy)
    controller = CreateTaskController(usecase_spy)
    controller.handle(description)

    assert usecase_spy.execute_called is True
    assert isinstance(
        usecase_spy.execute_called_with["request"], CreateTaskRequest
    )
    assert (
        usecase_spy.execute_called_with["request"].description == description
    )
