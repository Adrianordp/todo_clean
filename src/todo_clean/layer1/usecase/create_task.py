from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo


class CreateNewTask:
    def __init__(self, task: Task, task_repo: ITaskRepo):
        self.task = task
        self.task_repo = task_repo

    def execute(self):
        return self.task_repo.new_task(self.task.description)
