from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskInputData,
    CreateTaskOutputData,
    ICreateTask,
)
from src.todo_clean.layer2.controller.create_task_controller import CreateTaskController


class TaskRepoMock(ITaskRepo):
    def new_task(self, description: str) -> Task:
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
    def __init__(self, task_repo: ITaskRepo):
        pass

    def execute(self, input_data: CreateTaskInputData) -> CreateTaskOutputData:
        return CreateTaskOutputData(Task(1, input_data.description))


def test_controller_create_task():
    task_repo_stub = TaskRepoMock()
    description = "Random task description"

    usecase_mock = CreateNewTaskSpy(task_repo_stub)
    controller = CreateTaskController(usecase_mock)
    output_data = controller.handle(description)

    assert isinstance(output_data, Task)
    assert output_data.description == description
