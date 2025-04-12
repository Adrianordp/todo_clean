from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo


class GetTasks:
    def __init__(self, task_repo: ITaskRepo):
        self.task_repo = task_repo

    def execute(self) -> list[Task]:
        return self.task_repo.get_tasks()
