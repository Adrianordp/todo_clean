"""
Presenter for get tasks use case.
"""

import json

from todo_clean.layer1.usecase.get_tasks import (
    GetTasksResponse,
    GetTasksViewModel,
    IGetTasksPresenter,
)


class GetTasksGuiPresenter(IGetTasksPresenter):
    """
    Presenter for get tasks use case.
    """

    view_model: GetTasksViewModel

    def format(self, response: GetTasksResponse) -> None:
        output_data = {}
        for task in response.task_list:
            output_data[task[0]] = {
                "description": task[1],
            }
        output_str = json.dumps(output_data)
        GetTasksGuiPresenter.view_model = GetTasksViewModel(output_str)
