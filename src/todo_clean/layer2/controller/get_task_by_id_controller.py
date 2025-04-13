from abc import ABC, abstractmethod

from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.usecase.get_task_by_id import GetTaskByIdInputData, IGetTask


class IGetTaskByIdController(ABC):
    @abstractmethod
    def __init__(self, usecase: IGetTask):
        pass

    @abstractmethod
    def handle(
        self,
        id_: int,
    ) -> ITask:
        pass


class GetTaskByIdController(IGetTaskByIdController):
    def __init__(self, usecase: IGetTask):
        self.usecase = usecase

    def handle(
        self,
        id_: int,
    ) -> ITask:
        input_data = GetTaskByIdInputData(id_)
        output_data = self.usecase.execute(input_data)
        return output_data.task
