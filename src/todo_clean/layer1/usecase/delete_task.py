from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo

class DeleteTask():
    def __init__(self, task: Task, task_repo: ITaskRepo):
        self.task = task
        self.task_repo = task_repo

    def execute(self):
        return self.task_repo.delete_task_by_id(self.task.id_)
