from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo


@dataclass
class GetTaskByIdInputData:
    id_: int


@dataclass
class GetTaskByIdOutputData:
    task: Task


class IGetTask(ABC):
    @abstractmethod
    def __init__(self, data: GetTaskByIdInputData, task_repo: ITaskRepo):
        pass

    @abstractmethod
    def execute(self) -> GetTaskByIdOutputData:
        pass


class GetTaskById(IGetTask):
    def __init__(self, input_data: GetTaskByIdInputData, task_repo: ITaskRepo):
        self.input_data = input_data
        self.task_repo = task_repo

    def execute(self) -> GetTaskByIdOutputData:
        task = self.task_repo.get_task_by_id(self.input_data.id_)
        return GetTaskByIdOutputData(task)
