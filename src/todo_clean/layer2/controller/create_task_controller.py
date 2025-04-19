"""
controller/create_task_controller.py

Controller for creating task use case."""

from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskRequest,
    ICreateTask,
)


class CreateTaskController:
    """Controller for creating task use case."""

    def __init__(self, usecase: ICreateTask):
        self.usecase = usecase

    def handle(self, description: str) -> None:
        """Handle creating task use case."""
        input_data = CreateTaskRequest(description)
        self.usecase.execute(input_data)
