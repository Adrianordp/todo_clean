"""
controller/delete_task_by_id_controller.py

Controller for deleting task use case.
"""

from todo_clean.layer1 import DeleteTaskByIdRequest, IDeleteTaskById


class DeleteTaskByIdController:
    """
    Controller for deleting task use case.

    :param IDeleteTaskById usecase: The use case for deleting task.
    """

    def __init__(self, usecase: IDeleteTaskById):
        self.usecase = usecase

    def handle(self, description: str) -> None:
        """
        Handle deleting task use case.
        """
        request = DeleteTaskByIdRequest(description)
        self.usecase.execute(request)
