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


class IGetTaskByIdPresenter(ABC):
    @abstractmethod
    def format(self, output_data: GetTaskByIdOutputData) -> dict:
        pass


class IGetTask(ABC):
    @abstractmethod
    def __init__(self, task_repo: ITaskRepo, presenter: IGetTaskByIdPresenter):
        pass

    @abstractmethod
    def execute(self, input_data: GetTaskByIdInputData) -> None:
        pass


class GetTaskById(IGetTask):
    def __init__(self, task_repo: ITaskRepo, presenter: IGetTaskByIdPresenter):
        self.task_repo = task_repo
        self.presenter = presenter

    def execute(self, input_data: GetTaskByIdInputData) -> None:
        task = self.task_repo.get_task_by_id(input_data.id_)
        output_data = GetTaskByIdOutputData(task)
        self.presenter.format(output_data)
