from abc import ABC, abstractmethod

from todo_clean.layer1.usecase.get_task_by_id import (
    GetTaskByIdInputData,
    IGetTaskById,
)


class IGetTaskByIdController(ABC):
    @abstractmethod
    def __init__(self, usecase: IGetTaskById):
        pass

    @abstractmethod
    def handle(self, id_: int) -> None:
        pass


class GetTaskByIdController(IGetTaskByIdController):
    def __init__(self, usecase: IGetTaskById):
        self.usecase = usecase

    def handle(self, id_: int) -> None:
        input_data = GetTaskByIdInputData(id_)
        self.usecase.execute(input_data)
