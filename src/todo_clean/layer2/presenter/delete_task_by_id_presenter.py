"""
presenter/delete_task_by_id_presenter.py

Presenter for deleting task use case.
"""

import json

from todo_clean.layer1 import (
    DeleteTaskByIdResponse,
    DeleteTaskByIdViewModel,
    IDeleteTaskByIdPresenter,
)


class DeleteTaskByIdGuiPresenter(IDeleteTaskByIdPresenter):
    """
    Presenter for deleting task use case.
    """

    view_model: DeleteTaskByIdViewModel

    def format(self, response: DeleteTaskByIdResponse) -> None:
        output_data = {"success": response.success}
        output_str = json.dumps(output_data)
        DeleteTaskByIdGuiPresenter.view_model = DeleteTaskByIdViewModel(
            output_str
        )
