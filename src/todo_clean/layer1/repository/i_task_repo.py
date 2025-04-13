from abc import ABC, abstractmethod

from ...layer0.entity.task import ITask


class ITaskRepo(ABC):
    @abstractmethod
    def create_task(self, description: str) -> ITask:
        pass

    @abstractmethod
    def get_task_by_id(self, _id: int) -> ITask:
        pass

    @abstractmethod
    def get_tasks(self) -> list[ITask]:
        pass

    @abstractmethod
    def edit_task_by_id(self, id_: int) -> ITask:
        pass

    @abstractmethod
    def delete_task_by_id(self, id_: int) -> bool:
        pass
