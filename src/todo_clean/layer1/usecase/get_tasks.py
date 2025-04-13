from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import ITask
from ..repository.i_task_repo import ITaskRepo


@dataclass
class GetTasksOutputData:
    tasks: list[ITask]


class IGetTasksPresenter(ABC):
    @abstractmethod
    def format(self, output_data: GetTasksOutputData) -> dict:
        pass


class IGetTasks(ABC):
    @abstractmethod
    def execute(self) -> GetTasksOutputData:
        pass


class GetTasks:
    def __init__(self, task_repo: ITaskRepo):
        self.task_repo = task_repo

    def execute(self) -> GetTasksOutputData:
        response = self.task_repo.get_tasks()
        return GetTasksOutputData(response)
