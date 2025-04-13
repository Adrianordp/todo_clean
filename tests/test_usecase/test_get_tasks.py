from src.todo_clean.layer0.entity.task import ITask, Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_tasks import (
    GetTasks,
    GetTasksOutputData,
    IGetTasksPresenter,
)


def test_get_tasks():

    class TaskRepoSpy(ITaskRepo):
        get_tasks_called = False

        def create_task(self, description: str) -> ITask:
            pass

        def get_task_by_id(self, id_: int) -> ITask:
            pass

        def get_tasks(self) -> list[ITask]:
            self.get_tasks_called = True

        def edit_task_by_id(self, id_: int) -> ITask:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            pass

    class GetTasksPresenterSpy(IGetTasksPresenter):
        format_called = False
        format_called_with = {}

        def format(self, output_data: GetTasksOutputData) -> None:
            self.format_called = True
            self.format_called_with["output_data"] = output_data

    task_repo_spy = TaskRepoSpy()
    presenter_spy = GetTasksPresenterSpy()

    usecase = GetTasks(task_repo_spy, presenter_spy)
    usecase.execute()

    assert task_repo_spy.get_tasks_called == True

    assert presenter_spy.format_called == True
    assert presenter_spy.format_called_with["output_data"] is not None
    assert isinstance(
        presenter_spy.format_called_with["output_data"], GetTasksOutputData
    )
