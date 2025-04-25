"""
usecase/create_task.py

Use case for creating a task.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...layer0.entity.task import ITask


@dataclass
class CreateTaskRequest:
    """
    Input data for creating task use case.

    :param str description: The description of the task.
    """

    description: str


@dataclass
class CreateTaskResponse:
    """
    Response for creating task use case.

    :param int id_: The id of the task.
    :param str description: The description of the task.
    """

    id_: int
    description: str


class ICreateTaskRepository(ABC):
    """
    Interface for repository for creating a task.
    """

    @abstractmethod
    def create_task(self, description: str) -> ITask:
        """Create a task in repository.

        :param str description: The description of the task.

        :return ITask: The created task.
        """


@dataclass
class CreaTaskViewModel:
    """
    ViewModel for creating task use case.

    :param int id: The id of the task.
    :param str description: The description of the task.
    """

    id: int
    description: str


class ICreateTaskPresenter(ABC):
    """
    Presenter for creating task use case.
    """

    view_model: CreaTaskViewModel

    @abstractmethod
    def format(self, response: CreateTaskResponse) -> None:
        """
        Format response for creating task use case.

        :param CreateTaskResponse response: The response for creating task use
        case.
        """

    @classmethod
    def get_view_model(cls) -> CreaTaskViewModel:
        """
        Get view model for creating task use case.

        :return CreaTaskViewModel: The view model for creating task use case.
        """
        return cls.view_model


class ICreateTask(ABC):
    """
    Interface for use case for creating a task.

    :param ICreateTaskRepository task_repo: The repository for creating a task.
    :param ICreateTaskPresenter presenter: The presenter for creating a task.
    """

    @abstractmethod
    def __init__(
        self,
        repository: ICreateTaskRepository,
        presenter: ICreateTaskPresenter,
    ):
        self.repository = repository
        self.presenter = presenter

    @abstractmethod
    def execute(self, request: CreateTaskRequest) -> None:
        """
        Execute creating task use case.

        :param CreateTaskRequest request: The request for creating task use
        case.
        """

    def get_presenter(self) -> ICreateTaskPresenter:
        """Get presenter for creating task use case."""
        return self.presenter


class CreateTask(ICreateTask):
    """Use case for creating a task."""

    def __init__(
        self,
        repository: ICreateTaskRepository,
        presenter: ICreateTaskPresenter,
    ):
        self.repository = repository
        self.presenter = presenter

    def execute(self, request: CreateTaskRequest) -> None:
        task = self.repository.create_task(request.description)
        response = CreateTaskResponse(task.id_, task.description)
        self.presenter.format(response)
