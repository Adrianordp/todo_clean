from abc import ABC, abstractmethod

from ...layer0.entity.task import Task


class ITaskRepo(ABC):
    @abstractmethod
    def create_task(self, description: str) -> Task:
        pass

    @abstractmethod
    def get_task_by_id(self, _id: int) -> Task:
        pass

    @abstractmethod
    def get_tasks(self) -> list[Task]:
        pass

    @abstractmethod
    def edit_task_by_id(self, id_: int) -> Task:
        pass

    @abstractmethod
    def delete_task_by_id(self, id_: int) -> bool:
        pass
