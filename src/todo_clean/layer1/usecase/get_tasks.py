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
    def execute(self) -> None:
        pass


class GetTasks:
    def __init__(self, task_repo: ITaskRepo, presenter: IGetTasksPresenter):
        self.task_repo = task_repo
        self.presenter = presenter

    def execute(self) -> None:
        response = self.task_repo.get_tasks()
        output_data = GetTasksOutputData(response)
        self.presenter.format(output_data)
