from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_task_by_id import (
    GetTaskByIdInputData,
    GetTaskByIdOutputData,
    IGetTaskById,
)
from src.todo_clean.layer2.controller.get_task_by_id_controller import (
    GetTaskByIdController,
)


class TaskRepoSpy(ITaskRepo):
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


class GetTaskByIdSpy(IGetTaskById):
    init_called = False
    init_called_with = {}
    execute_called = False
    execute_called_with = {}

    def __init__(self, task_repo: ITaskRepo):
        self.init_called = True
        self.init_called_with["task_repo"] = task_repo

    def execute(
        self, input_data: GetTaskByIdInputData
    ) -> GetTaskByIdOutputData:
        self.execute_called = True
        self.execute_called_with["input_data"] = input_data


def test_controller_get_task_by_id():
    id_ = 1

    task_repo_spy = TaskRepoSpy()
    usecase_spy = GetTaskByIdSpy(task_repo_spy)

    controller = GetTaskByIdController(usecase_spy)

    controller.handle(id_)

    assert usecase_spy.init_called is True
    assert usecase_spy.init_called_with["task_repo"] == task_repo_spy

    assert usecase_spy.execute_called is True
    assert isinstance(
        usecase_spy.execute_called_with["input_data"], GetTaskByIdInputData
    )
    assert usecase_spy.execute_called_with["input_data"].id_ == id_
