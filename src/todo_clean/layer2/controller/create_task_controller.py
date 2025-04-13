from abc import ABC, abstractmethod

from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskInputData,
    CreateTaskOutputData,
    ICreateTask,
)


class IController(ABC):
    @abstractmethod
    def __init__(self, usecase: ICreateTask):
        pass

    @abstractmethod
    def handle(
        self,
        description: str,
    ) -> Task:
        pass


class CreateTaskController(IController):
    def __init__(self, usecase: ICreateTask):
        self.usecase = usecase

    def handle(
        self,
        description: str,
    ) -> Task:
        input_data = CreateTaskInputData(description)
        output_data = self.usecase.execute(input_data)
        return output_data.task
