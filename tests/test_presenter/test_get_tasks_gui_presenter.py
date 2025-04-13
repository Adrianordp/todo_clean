from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer2.presenter.get_tasks_presenter import (
    GetTasksGuiPresenter,
    GetTasksOutputData,
)


def test_create_task_gui_presenter():
    task1 = Task(1, "Random task description task 1")
    task2 = Task(47, "Random task description task 2")
    tasks = [task1, task2]
    output_data = GetTasksOutputData(tasks)

    presenter = GetTasksGuiPresenter()
    response = presenter.format(output_data)

    assert response == {
        1: {"description": "Random task description task 1"},
        47: {"description": "Random task description task 2"},
    }
