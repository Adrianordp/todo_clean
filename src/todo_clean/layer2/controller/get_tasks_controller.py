from abc import ABC, abstractmethod

from todo_clean.layer1.usecase.get_tasks import IGetTasks


class IGetTasksController(ABC):
    @abstractmethod
    def __init__(self, usecase: IGetTasks):
        pass

    @abstractmethod
    def handle(self) -> None:
        pass


class GetTasksController(IGetTasksController):
    def __init__(self, usecase: IGetTasks):
        self.usecase = usecase

    def handle(self) -> None:
        self.usecase.execute()
