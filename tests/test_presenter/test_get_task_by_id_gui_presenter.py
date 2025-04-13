from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer2.presenter.get_task_by_id_presenter import (
    GetTaskByIdGuiPresenter,
)


def test_create_task_gui_presenter():
    task = Task(1, "Random task description")
    presenter = GetTaskByIdGuiPresenter()
    response = presenter.format(task)

    assert response == {"id": 1, "description": "Random task description"}
