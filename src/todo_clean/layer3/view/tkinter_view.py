"""Tkinter view for the TODO Clean application."""

from tkinter import Button, Entry, Tk

from todo_clean.layer1.usecase.create_task import ICreateTaskPresenter
from todo_clean.layer2.controller.create_task_controller import (
    CreateTaskController,
)


class TkinterView:
    """Tkinter view for the TODO Clean application."""

    def __init__(
        self,
        root: Tk,
    ):
        self.root = root

        self.create_task_controller: CreateTaskController
        self.create_task_presenter: ICreateTaskPresenter

        self.root.title("TODO Clean")
        self.root.geometry("400x400")

        self.create_task_entry = Entry(self.root)
        self.create_task_entry.pack()

        self.create_task_button = Button(
            self.root, text="Create Task", command=self.handle_create_task
        )
        self.create_task_button.pack()

    def handle_create_task(self):
        """Handle creating a task."""
        description = self.create_task_entry.get()
        self.create_task_controller.handle(description)
        view_model = self.create_task_presenter.get_view_model()
        print(view_model.description)

    def run(self):
        """Run the Tkinter view."""
        self.root.mainloop()

    def set_create_task_controller(self, controller: CreateTaskController):
        """Set the create task controller."""
        self.create_task_controller = controller
        self.create_task_presenter = controller.usecase.get_presenter()
