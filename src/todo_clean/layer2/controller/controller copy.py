from abc import ABC, abstractmethod

from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskInputData,
    CreateTaskOutputData,
    ICreateTask,
)
from src.todo_clean.layer1.usecase.delete_task import DeleteTaskData, IDeleteTask
from src.todo_clean.layer1.usecase.get_task import GetTaskByIdInputData, IGetTask
from src.todo_clean.layer1.usecase.get_tasks import IGetTasks


class IController(ABC):
    @abstractmethod
    def create_new_task(
        self,
        description: str,
        create_new_task_input_data: CreateTaskInputData,
        create_new_task: ICreateTask,
    ) -> CreateTaskOutputData:
        pass

    @abstractmethod
    def get_tasks(self) -> list[Task]:
        pass

    @abstractmethod
    def get_task_by_id(self, id_: int) -> Task:
        pass

    @abstractmethod
    def delete_task(self, id_: int) -> bool:
        pass


class Controller(IController):
    create_new_task_input_data: CreateTaskInputData
    create_new_task_output_data: CreateTaskOutputData
    get_task_data: GetTaskByIdInputData
    delete_task_data: DeleteTaskData

    def create_new_task(
        self,
        usecase: ICreateTask,
    ) -> Task:
        self.create_new_task_output_data = usecase.execute()
        return self.create_new_task_output_data.task

    def get_tasks(self) -> list[Task]:
        pass
        # self.usecase_get_tasks = IGetTasks(self.task_repo)
        # return self.usecase_get_tasks.execute()

    def get_task_by_id(self, id_: int) -> Task:
        pass
        # self.get_task_data.id_ = id_
        # self.usecase_get_task = IGetTask(self.get_task_data, self.task_repo)
        # return self.usecase_get_task.execute(id_)

    def delete_task(self, id_: int) -> bool:
        pass
        # self.delete_task_data.id_ = id_
        # self.usecase_delete_task = IDeleteTask(self.delete_task_data, self.task_repo)
        # return self.usecase_delete_task.execute(id_)
