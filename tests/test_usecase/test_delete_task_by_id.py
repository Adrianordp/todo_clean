from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.delete_task_by_id import (
    DeleteTaskById,
    DeleteTaskByIdInputData,
    DeleteTaskByIdOutputData,
    IDeleteTaskByIdPresenter,
)


def test_usecase_delete_task_by_id():

    class TaskRepoSpy(ITaskRepo):
        delete_task_by_id_called = False
        delete_task_by_id_called_with = {}

        def create_task(self, description: str) -> ITask:
            pass

        def get_task_by_id(self, id_: int) -> ITask:
            pass

        def get_tasks(self) -> list[ITask]:
            pass

        def edit_task_by_id(self, id_: int) -> ITask:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            self.delete_task_by_id_called = True
            self.delete_task_by_id_called_with["id_"] = id_

    class DeleteTaskPresenterSpy(IDeleteTaskByIdPresenter):
        format_called = False
        format_called_with = {}

        def format(self, output_data: DeleteTaskByIdOutputData) -> None:
            self.format_called = True
            self.format_called_with["output_data"] = output_data

    id_ = 1
    presenter_spy = DeleteTaskPresenterSpy()
    input_data = DeleteTaskByIdInputData(id_)
    task_repo_spy = TaskRepoSpy()
    usecase = DeleteTaskById(task_repo_spy, presenter_spy)
    usecase.execute(input_data)

    assert task_repo_spy.delete_task_by_id_called
    assert task_repo_spy.delete_task_by_id_called_with["id_"] == id_

    assert presenter_spy.format_called == True
    assert presenter_spy.format_called_with["output_data"] is not None
    assert isinstance(
        presenter_spy.format_called_with["output_data"],
        DeleteTaskByIdOutputData,
    )
