from src.todo_clean.layer1.usecase.create_new_task import CreateNewTask
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer0.entity.task import Task


class SpyTaskRepo(ITaskRepo):
    description: str

    def new_task(self, description: str) -> Task:
        self.description = description
        return Task(1, description)

    def get_task_by_id(self) -> Task:
        pass

    def get_tasks(self) -> list[Task]:
        pass

    def edit_task_by_id(self, id_: int) -> Task:
        pass

    def delete_task(self, id_: int) -> bool:
        pass

def test_usecase_create_new_task():
    task = Task(1, "Random Task")
    task_repo = SpyTaskRepo()
    usecase = CreateNewTask(task, task_repo)
    response = usecase.execute()
    assert response.description == task.description
    assert task_repo.description == task.description
