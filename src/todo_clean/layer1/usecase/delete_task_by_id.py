"""
usecase/delete_task_by_id.py

Use case for deleting a task.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class DeleteTaskByIdRequest:
    """
    Input data for delete task use case.

    :param int id_: The id of the task.
    """

    id_: int


@dataclass
class DeleteTaskByIdResponse:
    """
    Output data for delete task use case.

    :param str success: The success of the operation.
    """

    success: bool


class IDeleteTaskByIdRepository(ABC):
    """
    Interface for repository for creating a task.
    """

    @abstractmethod
    def delete_task_by_id(self, id_: int) -> bool:
        """
        Delete task from repository.

        :param int id_: The id of the task.

        :return bool: The success of the operation.
        """


@dataclass
class DeleteTaskByIdViewModel:
    """
    ViewModel for delete task use case.

    :param str message: The message in JSON format.
    """

    message: str


class IDeleteTaskByIdPresenter(ABC):
    """
    Presenter for delete task use case.
    """

    view_model: DeleteTaskByIdViewModel

    @abstractmethod
    def format(self, response: DeleteTaskByIdResponse) -> None:
        """
        Format output data for delete task use case.

        :param DeleteTaskByIdResponse response: The response for delete task use case.
        """

    @classmethod
    def get_view_model(cls) -> DeleteTaskByIdViewModel:
        """
        Get view model for delete task use case.

        :return DeleteTaskByIdViewModel: The view model for delete task use case.
        """
        return cls.view_model


class IDeleteTaskById(ABC):
    """
    Interface for use case for deleting task.

    :param IDeleteTaskByIdRepository repository: The repository for deleting task.
    :param IDeleteTaskByIdPresenter presenter: The presenter for deleting task.
    """

    @abstractmethod
    def __init__(
        self,
        repository: IDeleteTaskByIdRepository,
        presenter: IDeleteTaskByIdPresenter,
    ):
        self.repository = repository
        self.presenter = presenter

    @abstractmethod
    def execute(self, request: DeleteTaskByIdRequest) -> None:
        """
        Execute delete task use case.

        :param DeleteTaskByIdRequest request: The request for delete task use
        case.
        """

    def get_presenter(self) -> IDeleteTaskByIdPresenter:
        """Get presenter for delete task use case."""
        return self.presenter


class DeleteTaskById(IDeleteTaskById):
    """
    Use case for deleting task.

    :param IDeleteTaskByIdRepository repository: The repository for deleting
    task.
    :param IDeleteTaskByIdPresenter presenter: The presenter for deleting task.
    """

    def __init__(
        self,
        repository: IDeleteTaskByIdRepository,
        presenter: IDeleteTaskByIdPresenter,
    ):
        self.repository = repository
        self.presenter = presenter

    def execute(self, request: DeleteTaskByIdRequest) -> None:
        """
        Execute delete task use case.
        """
        success = self.repository.delete_task_by_id(request.id_)
        response = DeleteTaskByIdResponse(success)
        self.presenter.format(response)
