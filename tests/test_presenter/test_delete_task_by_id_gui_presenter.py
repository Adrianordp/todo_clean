"""
presenter/delete_task_by_id_presenter.py

Presenter for deleting task use case.
"""

from todo_clean.layer1 import DeleteTaskByIdResponse, DeleteTaskByIdViewModel
from todo_clean.layer2 import DeleteTaskByIdGuiPresenter


def test_delete_task_by_id_gui_presenter():
    """
    Test presenter for creating task use case.
    """
    view_model = DeleteTaskByIdViewModel('{"success": true}')
    create_task_response = DeleteTaskByIdResponse(True)
    presenter = DeleteTaskByIdGuiPresenter()
    presenter.format(create_task_response)

    assert isinstance(presenter.view_model, DeleteTaskByIdViewModel)
    assert presenter.view_model == view_model


def test_delete_task_by_id_gui_presenter_unhappy():
    """
    Test presenter for creating task use case.
    """
    view_model = DeleteTaskByIdViewModel('{"success": false}')
    create_task_response = DeleteTaskByIdResponse(False)
    presenter = DeleteTaskByIdGuiPresenter()
    presenter.format(create_task_response)

    assert isinstance(presenter.view_model, DeleteTaskByIdViewModel)
    assert presenter.view_model == view_model
