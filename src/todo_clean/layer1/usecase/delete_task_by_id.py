from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo


@dataclass
class DeleteTaskInputData:
    id_: int


@dataclass
class DeleteTaskOutputData:
    success: bool


class IDeleteTask(ABC):
    @abstractmethod
    def __init__(self, task_repo: ITaskRepo):
        pass

    @abstractmethod
    def execute(self, input_data: DeleteTaskInputData) -> DeleteTaskOutputData:
        pass


class DeleteTask(IDeleteTask):
    def __init__(self, task_repo: ITaskRepo):
        self.task_repo = task_repo

    def execute(self, input_data: DeleteTaskInputData) -> DeleteTaskOutputData:
        success = self.task_repo.delete_task_by_id(input_data.id_)
        return DeleteTaskOutputData(success)
