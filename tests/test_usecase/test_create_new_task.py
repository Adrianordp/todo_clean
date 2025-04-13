from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.create_task import (
    CreateTask,
    CreateTaskInputData,
    CreateTaskOutputData,
)


def test_usecase_create_new_task():

    class SpyTaskRepo(ITaskRepo):
        description: str

        def new_task(self, description: str) -> Task:
            self.description = description
            return Task(1, description)

        def get_task_by_id(self, id_: int) -> Task:
            pass

        def get_tasks(self) -> list[Task]:
            pass

        def edit_task_by_id(self, id_: int) -> Task:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            pass

    description = "Random Task"
    input_data = CreateTaskInputData(description)
    task_repo_spy = SpyTaskRepo()
    usecase = CreateTask(task_repo_spy)
    response = usecase.execute(input_data)

    assert isinstance(response, CreateTaskOutputData)
    assert response.task.description == description
    assert task_repo_spy.description == description
