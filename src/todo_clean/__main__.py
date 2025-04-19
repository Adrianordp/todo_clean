"""Main module."""

import sqlite3
from tkinter import Tk

from todo_clean.layer1.usecase.create_task import CreateTask
from todo_clean.layer2.controller.create_task_controller import (
    CreateTaskController,
)
from todo_clean.layer2.presenter.create_task_presenter import (
    CreateTaskGuiPresenter,
)
from todo_clean.layer3.repository.create_task_repository import (
    CreateTaskSqliteRepository,
)
from todo_clean.layer3.view.tkinter_view import TkinterView


def main():
    """Main function."""
    conn = sqlite3.connect(":memory:")
    create_task_repo = CreateTaskSqliteRepository(conn)
    create_task_presenter = CreateTaskGuiPresenter()
    create_task_use_case = CreateTask(create_task_repo, create_task_presenter)
    controller = CreateTaskController(create_task_use_case)
    root = TkinterView(Tk())
    root.set_create_task_controller(controller)
    root.run()


if __name__ == "__main__":
    main()
