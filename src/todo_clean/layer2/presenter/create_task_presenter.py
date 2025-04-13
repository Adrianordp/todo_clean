from abc import ABC, abstractmethod

from src.todo_clean.layer0.entity.task import Task


class ICreateTaskPresenter(ABC):
    @abstractmethod
    def format(self, output_data: Task) -> dict:
        pass


class CreateTaskGuiPresenter(ICreateTaskPresenter):
    def format(self, output_data: Task) -> dict:
        return {"id": output_data.id_, "description": output_data.description}
