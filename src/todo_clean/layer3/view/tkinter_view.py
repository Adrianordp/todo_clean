"""
Tkinter view for the TODO Clean application.
"""

from tkinter import Button, Entry, Tk

from todo_clean.layer2 import CreateTaskController, GetTasksController


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

        self.root.title("TODO Clean")
        self.root.geometry("400x400")

        self.create_task_entry = Entry(self.root)
        self.create_task_entry.pack()

        self.create_task_button = Button(
            self.root, text="Create Task", command=self.handle_create_task
        )
        self.create_task_button.pack()

        self.get_tasks_button = Button(
            self.root, text="Get Tasks", command=self.handle_get_tasks
        )
        self.get_tasks_button.pack()

    def handle_create_task(self) -> None:
        """
        Handle creating a task.
        """
        description = self.create_task_entry.get()

        self.create_task_controller.handle(description)
        presenter = self.create_task_controller.usecase.get_presenter()
        view_model = presenter.get_view_model()

        print(view_model.description)

    def handle_get_tasks(self) -> None:
        """
        Handle getting tasks.
        """
        self.get_tasks_controller.handle()
        presenter = self.get_tasks_controller.usecase.get_presenter()
        view_model = presenter.get_view_model()

        print(view_model.tasks)

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

    def set_get_tasks_controller(self, controller: GetTasksController) -> None:
        """
        Set the get tasks controller.
        """
        self.get_tasks_controller = controller
