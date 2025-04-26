"""
controller/get_tasks_controller.py

Controller for getting tasks.
"""

from todo_clean.layer1.usecase.get_tasks import IGetTasks


class GetTasksController:
    """
    Controller for getting tasks.

    :param IGetTasks usecase: The use case for getting tasks.
    """

    def __init__(self, usecase: IGetTasks):
        self.usecase = usecase

    def handle(self) -> None:
        """
        Handle getting tasks use case.
        """
        self.usecase.execute()
