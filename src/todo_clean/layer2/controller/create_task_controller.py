"""
controller/create_task_controller.py

Controller for creating task use case.
"""

from todo_clean.layer1.usecase.create_task import (
    CreateTaskRequest,
    ICreateTask,
)


class CreateTaskController:
    """
    Controller for creating task use case.

    :param ICreateTask usecase: The use case for creating task.
    """

    def __init__(self, usecase: ICreateTask):
        self.usecase = usecase

    def handle(self, description: str) -> None:
        """
        Handle creating task use case.
        """
        request = CreateTaskRequest(description)
        self.usecase.execute(request)
