"""
presenter/create_task_presenter.py

Presenter for creating task use case.
"""

from todo_clean.layer1.usecase.create_task import CreateTaskResponse
from todo_clean.layer2.presenter.create_task_presenter import (
    CreaTaskViewModel,
    CreateTaskGuiPresenter,
)


def test_create_task_gui_presenter():
    """
    Test presenter for creating task use case.
    """
    view_model = CreaTaskViewModel(1, "Random task description")
    create_task_response = CreateTaskResponse(1, "Random task description")
    presenter = CreateTaskGuiPresenter()
    presenter.format(create_task_response)

    assert isinstance(presenter.view_model, CreaTaskViewModel)
    assert presenter.get_view_model() == view_model
