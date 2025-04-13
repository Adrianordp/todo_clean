from pytest import mark

from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_task import (
    GetTaskByIdInputData,
    GetTaskByIdOutputData,
    IGetTask,
)
from src.todo_clean.layer2.controller.get_task_by_id_controller import (
    GetTaskByIdController,
)


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


class GetTaskSpy(IGetTask):
    def __init__(self, task_repo: ITaskRepo):
        pass

    def execute(self, input_data: GetTaskByIdInputData) -> GetTaskByIdOutputData:
        return GetTaskByIdOutputData(Task(input_data.id_, ""))


def test_controller_get_task_by_id():
    id_ = 1

    task_repo_mock = TaskRepoMock()
    usecase_spy = GetTaskSpy(task_repo_mock)

    controller = GetTaskByIdController(usecase_spy)

    task = controller.handle(id_)

    assert isinstance(task, Task)
    assert task.id_ == id_
