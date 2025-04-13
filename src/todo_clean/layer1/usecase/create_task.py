from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import Task
from ..repository.i_task_repo import ITaskRepo


@dataclass
class CreateTaskInputData:
    description: str


@dataclass
class CreateTaskOutputData:
    task: Task


class ICreateTask(ABC):
    @abstractmethod
    def __init__(
        self,
        task_repo: ITaskRepo,
    ):
        pass

    @abstractmethod
    def execute(self, input_data: CreateTaskInputData) -> CreateTaskOutputData:
        pass


class CreateTask(ICreateTask):
    def __init__(
        self,
        task_repo: ITaskRepo,
    ):
        self.task_repo = task_repo

    def execute(self, input_data: CreateTaskInputData) -> CreateTaskOutputData:
        task = self.task_repo.new_task(input_data.description)
        return CreateTaskOutputData(task)
