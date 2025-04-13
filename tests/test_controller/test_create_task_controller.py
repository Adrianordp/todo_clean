from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskInputData,
    CreateTaskOutputData,
    ICreateTask,
)
from src.todo_clean.layer2.controller.create_task_controller import CreateTaskController


class TaskRepoDummy(ITaskRepo):
    def create_task(self, description: str) -> Task:
        pass

    def get_task_by_id(self, _id: int) -> Task:
        pass

    def get_tasks(self) -> list[Task]:
        pass

    def edit_task_by_id(self, id_: int) -> Task:
        pass

    def delete_task_by_id(self, id_: int) -> bool:
        pass


class CreateNewTaskSpy(ICreateTask):
    init_called = False
    init_called_with = {}
    execute_called = False
    execute_called_with = {}

    def __init__(self, task_repo: ITaskRepo):
        self.init_called = True
        self.init_called_with["task_repo"] = task_repo

    def execute(self, input_data: CreateTaskInputData) -> CreateTaskOutputData:
        self.execute_called = True
        self.execute_called_with["input_data"] = input_data
        return CreateTaskOutputData(Task(1, input_data.description))


def test_controller_create_task():
    task_repo_dummy = TaskRepoDummy()
    description = "Random task description"

    usecase_spy = CreateNewTaskSpy(task_repo_dummy)
    controller = CreateTaskController(usecase_spy)
    controller.handle(description)

    assert usecase_spy.init_called == True
    assert usecase_spy.init_called_with["task_repo"] == task_repo_dummy

    assert usecase_spy.execute_called == True
    assert usecase_spy.execute_called_with["input_data"].description == description
