from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..repository.i_task_repo import ITaskRepo


@dataclass
class DeleteTaskByIdInputData:
    id_: int


@dataclass
class DeleteTaskByIdOutputData:
    success: bool


class IDeleteTaskByIdPresenter(ABC):
    @abstractmethod
    def format(self, output_data: DeleteTaskByIdOutputData) -> None:
        pass


class IDeleteTaskById(ABC):
    @abstractmethod
    def __init__(
        self, task_repo: ITaskRepo, presenter: IDeleteTaskByIdPresenter
    ):
        pass

    @abstractmethod
    def execute(self, input_data: DeleteTaskByIdInputData) -> None:
        pass


class DeleteTaskById(IDeleteTaskById):
    def __init__(
        self, task_repo: ITaskRepo, presenter: IDeleteTaskByIdPresenter
    ):
        self.task_repo = task_repo
        self.presenter = presenter

    def execute(self, input_data: DeleteTaskByIdInputData) -> None:
        success = self.task_repo.delete_task_by_id(input_data.id_)
        output_data = DeleteTaskByIdOutputData(success)
        self.presenter.format(output_data)
