from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo


@dataclass
class DeleteTaskData:
    id_: int


class IDeleteTask(ABC):
    @abstractmethod
    def __init__(self, data: DeleteTaskData, task_repo: ITaskRepo):
        pass

    @abstractmethod
    def execute(self) -> bool:
        pass


class DeleteTask(IDeleteTask):
    def __init__(self, data: DeleteTaskData, task_repo: ITaskRepo):
        self.data = data
        self.task_repo = task_repo

    def execute(self) -> bool:
        return self.task_repo.delete_task_by_id(self.data.id_)
