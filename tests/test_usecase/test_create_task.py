from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.create_task import (
    CreateTask,
    CreateTaskInputData,
    CreateTaskOutputData,
    ICreateTaskPresenter,
)


def test_usecase_create_new_task():

    class TaskRepoSpy(ITaskRepo):
        new_task_called = False
        new_task_called_with = {}

        def create_task(self, description: str) -> Task:
            self.new_task_called = True
            self.new_task_called_with = description
            return Task(1, description)

        def get_task_by_id(self, id_: int) -> Task:
            pass

        def get_tasks(self) -> list[Task]:
            pass

        def edit_task_by_id(self, id_: int) -> Task:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            pass

    class CreateTaskPresenterSpy(ICreateTaskPresenter):
        format_called = False
        format_called_with = {}

        def format(self, output_data: CreateTaskOutputData) -> None:
            self.format_called = True
            self.format_called_with = output_data

    description = "Random Task"

    input_data = CreateTaskInputData(description)

    task_repo_spy = TaskRepoSpy()
    presenter_spy = CreateTaskPresenterSpy()

    usecase = CreateTask(task_repo_spy, presenter_spy)
    usecase.execute(input_data)

    assert task_repo_spy.new_task_called == True
    assert task_repo_spy.new_task_called_with == description

    assert presenter_spy.format_called == True
    assert presenter_spy.format_called_with.task.description == description
