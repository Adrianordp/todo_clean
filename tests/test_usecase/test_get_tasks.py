from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_tasks import GetTasks


def test_get_tasks():

    class SpyTaskRepo(ITaskRepo):
        task1 = Task(1, "Random Task")
        task2 = Task(2, "Random Task")
        task_list = [task1, task2]

        def new_task(self, description: str) -> Task:
            pass

        def get_task_by_id(self, id_: int) -> Task:
            pass

        def get_tasks(self) -> list[Task]:
            return self.task_list

        def edit_task_by_id(self, id_: int) -> Task:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            pass

    task_repo = SpyTaskRepo()
    usecase = GetTasks(task_repo)
    task_list = usecase.execute()
    assert task_list == task_repo.task_list
