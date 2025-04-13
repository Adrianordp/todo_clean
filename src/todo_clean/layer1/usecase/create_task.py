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


class ICreateTaskPresenter(ABC):
    @abstractmethod
    def format(self, output_data: CreateTaskOutputData) -> dict:
        pass


class ICreateTask(ABC):
    @abstractmethod
    def __init__(
        self,
        task_repo: ITaskRepo,
        presenter: ICreateTaskPresenter,
    ):
        pass

    @abstractmethod
    def execute(self, input_data: CreateTaskInputData) -> None:
        pass


class CreateTask(ICreateTask):
    def __init__(
        self,
        task_repo: ITaskRepo,
        presenter: ICreateTaskPresenter,
    ):
        self.task_repo = task_repo
        self.presenter = presenter

    def execute(self, input_data: CreateTaskInputData) -> None:
        task = self.task_repo.create_task(input_data.description)
        output_data = CreateTaskOutputData(task)
        self.presenter.format(output_data)
