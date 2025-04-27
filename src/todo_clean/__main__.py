"""Main module."""

import sqlite3
from tkinter import Tk

from todo_clean.layer1 import CreateTask, DeleteTaskById, GetTasks
from todo_clean.layer2 import (
    CreateTaskController,
    CreateTaskGuiPresenter,
    DeleteTaskByIdController,
    DeleteTaskByIdGuiPresenter,
    GetTasksController,
    GetTasksGuiPresenter,
)
from todo_clean.layer3 import (
    CreateTaskSqliteRepository,
    DeleteTaskByIdSqliteRepository,
    GetTasksSqliteRepository,
    TkinterView,
)


def main():
    """Main function."""
    conn = sqlite3.connect(":memory:")

    create_task_repo = CreateTaskSqliteRepository(conn)
    create_task_presenter = CreateTaskGuiPresenter()
    create_task_use_case = CreateTask(create_task_repo, create_task_presenter)
    create_task_controller = CreateTaskController(create_task_use_case)

    delete_task_repo = DeleteTaskByIdSqliteRepository(conn)
    delete_task_presenter = DeleteTaskByIdGuiPresenter()
    delete_task_use_case = DeleteTaskById(
        delete_task_repo, delete_task_presenter
    )
    delete_task_controller = DeleteTaskByIdController(delete_task_use_case)

    get_tasks_repo = GetTasksSqliteRepository(conn)
    get_tasks_presenter = GetTasksGuiPresenter()
    get_tasks_use_case = GetTasks(get_tasks_repo, get_tasks_presenter)
    get_tasks_controller = GetTasksController(get_tasks_use_case)

    root = TkinterView(Tk())
    root.set_create_task_controller(create_task_controller)
    root.set_get_tasks_controller(get_tasks_controller)
    root.set_delete_task_controller(delete_task_controller)
    root.run()


if __name__ == "__main__":
    main()
