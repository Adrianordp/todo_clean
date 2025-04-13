from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import ITask
from ..repository.i_task_repo import ITaskRepo


@dataclass
class GetTaskByIdInputData:
    id_: int


@dataclass
class GetTaskByIdOutputData:
    task: ITask


class IGetTask(ABC):
    @abstractmethod
    def __init__(self, task_repo: ITaskRepo):
        pass

    @abstractmethod
    def execute(
        self, input_data: GetTaskByIdInputData
    ) -> GetTaskByIdOutputData:
        pass


class GetTaskById(IGetTask):
    def __init__(self, task_repo: ITaskRepo):
        self.task_repo = task_repo

    def execute(
        self, input_data: GetTaskByIdInputData
    ) -> GetTaskByIdOutputData:
        task = self.task_repo.get_task_by_id(input_data.id_)
        return GetTaskByIdOutputData(task)
