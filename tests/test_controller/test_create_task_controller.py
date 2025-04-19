"""Test controller for creating a task."""

from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskRequest,
    CreateTaskResponse,
    ICreateTask,
    ICreateTaskPresenter,
    ICreateTaskRepository,
)
from src.todo_clean.layer2.controller.create_task_controller import (
    CreateTaskController,
)


class CreateTaskRepositoryDummy(ICreateTaskRepository):
    """Dummy for creating task repository."""

    def create_task(self, description: str) -> tuple[int, ITask]:
        pass


class CreateNewTaskSpy(ICreateTask):
    """Spy for creating task use case."""

    execute_called = False
    execute_called_with = {}

    def __init__(
        self, task_repo: ICreateTaskRepository, presenter: ICreateTaskPresenter
    ):
        pass

    def execute(self, request: CreateTaskRequest) -> None:
        self.execute_called = True
        self.execute_called_with["request"] = request


class PresenterDummy(ICreateTaskPresenter):
    """Dummy for creating task presenter."""

    def format(self, output_data: CreateTaskResponse) -> None:
        pass


def test_controller_create_task():
    """Test controller for creating a task."""
    description = "Random task description"
    task_repo_stub = CreateTaskRepositoryDummy()
    presenter_dummy = PresenterDummy()

    usecase_spy = CreateNewTaskSpy(task_repo_stub, presenter_dummy)
    controller = CreateTaskController(usecase_spy)
    controller.handle(description)

    assert usecase_spy.execute_called is True
    assert isinstance(
        usecase_spy.execute_called_with["request"], CreateTaskRequest
    )
    assert (
        usecase_spy.execute_called_with["request"].description == description
    )
