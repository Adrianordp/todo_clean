from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer2.presenter.create_task_presenter import (
    CreateTaskGuiPresenter,
)


def test_create_task_gui_presenter():
    task = Task(1, "Random task description")
    presenter = CreateTaskGuiPresenter()
    response = presenter.format(task)

    assert response == {"id": 1, "description": "Random task description"}
