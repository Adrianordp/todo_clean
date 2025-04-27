"""
Tkinter view for the TODO Clean application.
"""

import json
from tkinter import Button, Entry, Listbox, Tk

from todo_clean.layer2 import (
    CreateTaskController,
    DeleteTaskByIdController,
    GetTasksController,
)


class TkinterView:
    """
    Tkinter view for the TODO Clean application.
    """

    def __init__(
        self,
        root: Tk,
    ):
        self.root = root

        self.create_task_controller: CreateTaskController
        self.get_tasks_controller: GetTasksController
        self.delete_task_controller: DeleteTaskByIdController

        self.root.title("TODO Clean")
        self.root.geometry("400x400")

        self.task_array = []
        self.id_array = []

        self.create_task_entry = Entry(self.root)
        self.create_task_entry.pack()

        self.create_task_button = Button(
            self.root, text="Create Task", command=self._handle_create_task
        )
        self.create_task_button.pack()

        self.delete_task_button = Button(
            self.root, text="Delete Task", command=self._handle_delete_task
        )
        self.delete_task_button.pack()

        self.task_list = Listbox(self.root)
        self.task_list.pack()

    def _handle_create_task(self) -> None:
        """
        Handle creating a task.
        """
        description = self.create_task_entry.get()

        self.create_task_controller.handle(description)

        self._handle_get_tasks()

    def _handle_delete_task(self) -> None:
        """
        Handle deleting a task.
        """
        if len(self.task_list.curselection()) == 0:
            return
        idx = self.task_list.curselection()[0]
        id_ = self.id_array[idx]
        self.delete_task_controller.handle(id_)
        self._handle_get_tasks()

    def _handle_get_tasks(self) -> None:
        """
        Handle getting tasks.
        """
        self.get_tasks_controller.handle()
        presenter = self.get_tasks_controller.usecase.get_presenter()
        view_model = presenter.get_view_model()
        tasks_json: dict = json.loads(view_model.tasks)
        self.task_array = [
            description["description"] for _, description in tasks_json.items()
        ]
        self.id_array = [id for id, _ in tasks_json.items()]
        self.task_list.delete(0, "end")
        self.task_list.insert(0, *self.task_array)

    def run(self) -> None:
        """
        Run the Tkinter view.
        """
        self.root.mainloop()

    def set_create_task_controller(
        self, controller: CreateTaskController
    ) -> None:
        """
        Set the create task controller.
        """
        self.create_task_controller = controller

    def set_delete_task_controller(
        self, controller: DeleteTaskByIdController
    ) -> None:
        """
        Set the delete task controller.
        """
        self.delete_task_controller = controller

    def set_get_tasks_controller(self, controller: GetTasksController) -> None:
        """
        Set the get tasks controller.
        """
        self.get_tasks_controller = controller

        self._handle_get_tasks()
