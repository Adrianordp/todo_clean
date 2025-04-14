from abc import ABC, abstractmethod

from src.todo_clean.layer1.usecase.delete_task_by_id import (
    DeleteTaskByIdInputData,
    IDeleteTaskById,
)


class IDeleteTaskByIdController(ABC):
    @abstractmethod
    def __init__(self, usecase: IDeleteTaskById):
        pass

    @abstractmethod
    def handle(self, id_: int) -> None:
        pass


class DeleteTaskByIdController(IDeleteTaskByIdController):
    def __init__(self, usecase: IDeleteTaskById):
        self.usecase = usecase

    def handle(self, id_: int) -> None:
        input_data = DeleteTaskByIdInputData(id_)
        self.usecase.execute(input_data)
