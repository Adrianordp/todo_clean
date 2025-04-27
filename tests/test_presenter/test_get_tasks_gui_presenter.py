"""
presenter/get_tasks_presenter.py

Test presenter for get tasks use case.
"""

from todo_clean.layer2.presenter.get_tasks_presenter import (
    GetTasksGuiPresenter,
    GetTasksResponse,
    GetTasksViewModel,
)


def test_create_task_gui_presenter():
    """
    Test presenter for creating task use case.
    """
    task1 = (1, "Random task description task 1")
    task2 = (47, "Random task description task 2")
    tasks = [task1, task2]
    response = GetTasksResponse(tasks)

    presenter = GetTasksGuiPresenter()
    presenter.format(response)

    expected_string = (
        '{"1": {"description": "Random task description task 1"}, '
        '"47": {"description": "Random task description task 2"}}'
    )
    actual_view_model = presenter.get_view_model()
    expected_view_model = GetTasksViewModel(expected_string)
    assert actual_view_model.tasks == expected_string
    assert actual_view_model == expected_view_model
