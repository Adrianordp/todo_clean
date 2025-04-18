"""
usecase/create_task.py

Use case for creating a task.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import ITask


@dataclass
class CreateTaskRequest:
    """Input data for creating task use case."""

    description: str


@dataclass
class CreateTaskResponse:
    """Output data for creating task use case."""

    id_: int
    description: str


class ICreateTaskRepository(ABC):
    """Interface for repository for creating a task."""

    @abstractmethod
    def create_task(self, description: str) -> tuple[int, ITask]:
        """Create a task.

        Args:
            description (str): The description of the task.

        Returns:
            tuple[int, ITask]: The id of the created task and the task entity.
        """


class ICreateTaskPresenter(ABC):
    """Presenter for creating task use case."""

    @abstractmethod
    def format(self, output_data: CreateTaskResponse) -> None:
        """Format output data for creating task use case."""


class ICreateTask(ABC):
    """Interface for use case for creating a task."""

    @abstractmethod
    def __init__(
        self,
        request: CreateTaskRequest,
        task_repo: ICreateTaskRepository,
        presenter: ICreateTaskPresenter,
    ):
        pass

    @abstractmethod
    def execute(self) -> None:
        """Execute creating task use case."""


class CreateTask(ICreateTask):
    """Use case for creating a task."""

    def __init__(
        self,
        request: CreateTaskRequest,
        task_repo: ICreateTaskRepository,
        presenter: ICreateTaskPresenter,
    ):
        self.request = request
        self.task_repo = task_repo
        self.presenter = presenter

    def execute(self) -> None:
        id_, task = self.task_repo.create_task(self.request.description)
        output_data = CreateTaskResponse(id_, task.description)
        self.presenter.format(output_data)
