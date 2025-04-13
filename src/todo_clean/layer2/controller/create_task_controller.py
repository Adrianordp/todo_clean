from abc import ABC, abstractmethod

from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskInputData,
    ICreateTask,
)


class ICreateTaskController(ABC):
    @abstractmethod
    def __init__(self, usecase: ICreateTask):
        pass

    @abstractmethod
    def handle(
        self,
        description: str,
    ) -> None:
        pass


class CreateTaskController(ICreateTaskController):
    def __init__(self, usecase: ICreateTask):
        self.usecase = usecase

    def handle(
        self,
        description: str,
    ) -> None:
        input_data = CreateTaskInputData(description)
        self.usecase.execute(input_data)
