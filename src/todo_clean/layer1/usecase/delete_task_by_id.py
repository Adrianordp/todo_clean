from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..repository.i_task_repo import ITaskRepo


@dataclass
class DeleteTaskInputData:
    id_: int


@dataclass
class DeleteTaskOutputData:
    success: bool


class IDeleteTaskPresenter(ABC):
    @abstractmethod
    def format(self, output_data: DeleteTaskOutputData) -> None:
        pass


class IDeleteTask(ABC):
    @abstractmethod
    def __init__(self, task_repo: ITaskRepo, presenter: IDeleteTaskPresenter):
        pass

    @abstractmethod
    def execute(self, input_data: DeleteTaskInputData) -> None:
        pass


class DeleteTask(IDeleteTask):
    def __init__(self, task_repo: ITaskRepo, presenter: IDeleteTaskPresenter):
        self.task_repo = task_repo
        self.presenter = presenter

    def execute(self, input_data: DeleteTaskInputData) -> None:
        success = self.task_repo.delete_task_by_id(input_data.id_)
        output_data = DeleteTaskOutputData(success)
        self.presenter.format(output_data)
