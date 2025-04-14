from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskInputData,
    CreateTaskOutputData,
    ICreateTask,
    ICreateTaskPresenter,
)
from src.todo_clean.layer2.controller.create_task_controller import (
    CreateTaskController,
)


class TaskRepoDummy(ITaskRepo):
    def create_task(self, description: str) -> ITask:
        pass

    def get_task_by_id(self, _id: int) -> ITask:
        pass

    def get_tasks(self) -> list[ITask]:
        pass

    def edit_task_by_id(self, id_: int) -> ITask:
        pass

    def delete_task_by_id(self, id_: int) -> bool:
        pass


class CreateNewTaskSpy(ICreateTask):
    execute_called = False
    execute_called_with = {}

    def __init__(self, task_repo: ITaskRepo, presenter: ICreateTaskPresenter):
        pass

    def execute(self, input_data: CreateTaskInputData) -> None:
        self.execute_called = True
        self.execute_called_with["input_data"] = input_data


class PresenterDummy(ICreateTaskPresenter):
    def format(self, output_data: CreateTaskOutputData) -> dict:
        pass


def test_controller_create_task():
    description = "Random task description"
    task_repo_dummy = TaskRepoDummy()
    presenter_dummy = PresenterDummy()

    usecase_spy = CreateNewTaskSpy(task_repo_dummy, presenter_dummy)
    controller = CreateTaskController(usecase_spy)
    controller.handle(description)

    assert usecase_spy.execute_called is True
    assert (
        usecase_spy.execute_called_with["input_data"].description
        == description
    )
