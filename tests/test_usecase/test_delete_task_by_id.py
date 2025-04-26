"""
Test use case for deleting a task.
"""

from todo_clean.layer1.usecase.delete_task_by_id import (
    DeleteTaskById,
    DeleteTaskByIdRequest,
    DeleteTaskByIdResponse,
    IDeleteTaskByIdPresenter,
    IDeleteTaskByIdRepository,
)


class RepositoryStub(IDeleteTaskByIdRepository):
    """
    Stub for repository for deleting a task.
    """

    def __init__(self, fake_success: bool = True):
        self.delete_task_by_id_called = False
        self.delete_task_by_id_called_with = {}
        self.fake_success = fake_success

    def delete_task_by_id(self, id_: int) -> bool:
        self.delete_task_by_id_called = True
        self.delete_task_by_id_called_with["id_"] = id_
        return self.fake_success


class DeleteTaskPresenterSpy(IDeleteTaskByIdPresenter):
    """
    Spy for presenter for deleting a task.
    """

    format_called = False
    format_called_with = {}

    def format(self, response: DeleteTaskByIdResponse) -> None:
        self.format_called = True
        self.format_called_with["response"] = response


def test_usecase_delete_task_by_id():
    """
    Test use case for deleting a task.
    """
    id_ = 1
    success = True

    presenter_spy = DeleteTaskPresenterSpy()
    request = DeleteTaskByIdRequest(id_)
    task_repo_spy = RepositoryStub(success)

    usecase = DeleteTaskById(task_repo_spy, presenter_spy)
    usecase.execute(request)

    assert task_repo_spy.delete_task_by_id_called is True
    assert task_repo_spy.delete_task_by_id_called_with["id_"] == id_

    assert presenter_spy.format_called is True
    assert presenter_spy.format_called_with["response"] is not None
    assert isinstance(
        presenter_spy.format_called_with["response"],
        DeleteTaskByIdResponse,
    )
    assert presenter_spy.format_called_with["response"].success is success
    assert presenter_spy.format_called_with[
        "response"
    ] == DeleteTaskByIdResponse(success)

    assert usecase.get_presenter() == presenter_spy


def test_usecase_delete_task_by_id_unhappy():
    """
    Test use case for deleting a task.
    """
    id_ = 1
    success = False

    presenter_spy = DeleteTaskPresenterSpy()
    request = DeleteTaskByIdRequest(id_)
    task_repo_spy = RepositoryStub(success)

    usecase = DeleteTaskById(task_repo_spy, presenter_spy)
    usecase.execute(request)

    assert task_repo_spy.delete_task_by_id_called is True
    assert task_repo_spy.delete_task_by_id_called_with["id_"] == id_

    assert presenter_spy.format_called is True
    assert presenter_spy.format_called_with["response"] is not None
    assert isinstance(
        presenter_spy.format_called_with["response"],
        DeleteTaskByIdResponse,
    )
    assert presenter_spy.format_called_with["response"].success is success
    assert presenter_spy.format_called_with[
        "response"
    ] == DeleteTaskByIdResponse(success)

    assert usecase.get_presenter() == presenter_spy
