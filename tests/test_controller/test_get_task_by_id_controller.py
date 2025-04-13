from pytest import mark

from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_task import (
    GetTaskByIdInputData,
    GetTaskByIdOutputData,
    IGetTask,
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


class GetTaskSpy(IGetTask):
    def __init__(self, input_data: GetTaskByIdInputData, task_repo: ITaskRepo):
        self.input_data = input_data
        self.task_repo = task_repo

    def execute(self) -> GetTaskByIdOutputData:
        return GetTaskByIdOutputData(Task(1, ""))


@mark.skip
def test_controller_get_task_by_id():
    controller = CreateTaskController()

    task_repo_spy = TaskRepoMock()
    input_data = GetTaskByIdInputData(1)
    usecase_spy = GetTaskSpy(input_data, task_repo_spy)

    output_data = controller.get_task_by_id(usecase_spy)

    assert usecase_spy.input_data == input_data
    assert output_data.id_ == input_data.id_
