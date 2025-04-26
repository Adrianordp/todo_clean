"""
usecase/get_tasks.py

Use case for getting tasks.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from todo_clean.layer0.entity.task import ITask


@dataclass
class GetTasksViewModel:
    """
    ViewModel for get tasks use case.

    :param str tasks: The list of tasks in JSON format.
    """

    tasks: str


@dataclass
class GetTasksResponse:
    """
    Output data for get tasks use case.

    :param list[tuple[int, str]] task_list: The list of tasks.
    """

    task_list: list[tuple[int, str]]


class IGetTasksRepository(ABC):
    """
    Interface for repository for creating a task.
    """

    @abstractmethod
    def get_tasks(self) -> list[ITask]:
        """
        Get tasks from repository.

        :return list[ITask]: The list of tasks.
        """


class IGetTasksPresenter(ABC):
    """
    Presenter for get tasks use case.
    """

    view_model: GetTasksViewModel

    @abstractmethod
    def format(self, response: GetTasksResponse) -> None:
        """
        Format output data for get tasks use case.

        :param GetTasksResponse response: The response for get tasks use case.
        """

    @classmethod
    def get_view_model(cls) -> GetTasksViewModel:
        """
        Get view model for get tasks use case.

        :return GetTasksViewModel: The view model for get tasks use case.
        """
        return cls.view_model


class IGetTasks(ABC):
    """
    Interface for use case for getting tasks.

    :param IGetTasksRepository repository: The repository for getting tasks.
    :param IGetTasksPresenter presenter: The presenter for getting tasks.
    """

    @abstractmethod
    def __init__(
        self,
        repository: IGetTasksRepository,
        presenter: IGetTasksPresenter,
    ):
        self.repository = repository
        self.presenter = presenter

    @abstractmethod
    def execute(self) -> None:
        """
        Execute get tasks use case.
        """

    def get_presenter(self) -> IGetTasksPresenter:
        """Get presenter for creating task use case."""
        return self.presenter


class GetTasks(IGetTasks):
    """
    Use case for getting tasks.

    :param IGetTasksRepository repository: The repository for getting tasks.
    :param IGetTasksPresenter presenter: The presenter for getting tasks.
    """

    def __init__(
        self, repository: IGetTasksRepository, presenter: IGetTasksPresenter
    ):
        self.repository = repository
        self.presenter = presenter

    def execute(self) -> None:
        """
        Execute get tasks use case.
        """
        tasks = self.repository.get_tasks()
        response = [(task.id_, task.description) for task in tasks]
        output_data = GetTasksResponse(response)
        self.presenter.format(output_data)
