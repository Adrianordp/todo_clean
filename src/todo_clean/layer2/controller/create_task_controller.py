from abc import ABC, abstractmethod

from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.usecase.create_task import CreateTaskInputData, ICreateTask


class ICreateTaskController(ABC):
    @abstractmethod
    def __init__(self, usecase: ICreateTask):
        pass

    @abstractmethod
    def handle(
        self,
        description: str,
    ) -> Task:
        pass


class CreateTaskController(ICreateTaskController):
    def __init__(self, usecase: ICreateTask):
        self.usecase = usecase

    def handle(
        self,
        description: str,
    ) -> Task:
        input_data = CreateTaskInputData(description)
        output_data = self.usecase.execute(input_data)
        return output_data.task
