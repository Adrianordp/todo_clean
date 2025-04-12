from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo


class GetTask:
    def __init__(self, id_: int, task_repo: ITaskRepo):
        self.id_ = id_
        self.task_repo = task_repo

    def execute(self) -> Task:
        return self.task_repo.get_task_by_id(self.id_)
