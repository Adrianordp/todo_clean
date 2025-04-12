from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.delete_task import DeleteTask


def test_usecase_delete_task_by_id():

    class SpyTaskRepo(ITaskRepo):
        id_: int

        def new_task(self, description: str) -> Task:
            pass

        def get_task_by_id(self, id_: int) -> Task:
            pass

        def get_tasks(self) -> list[Task]:
            pass

        def edit_task_by_id(self, id_: int) -> Task:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            self.id_ = id_
            return True

    task = Task(1, "Random Task")
    task_repo = SpyTaskRepo()
    usecase = DeleteTask(task, task_repo)
    assert usecase.execute()
    assert task_repo.id_ == task.id_
