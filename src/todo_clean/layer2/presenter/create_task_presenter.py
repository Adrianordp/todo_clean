from abc import ABC, abstractmethod

from src.todo_clean.layer0.entity.task import ITask


class ICreateTaskPresenter(ABC):
    @abstractmethod
    def format(self, output_data: ITask) -> dict:
        pass


class CreateTaskGuiPresenter(ICreateTaskPresenter):
    def format(self, output_data: ITask) -> dict:
        return {"id": output_data.id_, "description": output_data.description}
