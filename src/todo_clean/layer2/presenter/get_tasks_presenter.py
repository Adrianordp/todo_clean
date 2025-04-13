from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.usecase.get_tasks import (
    GetTasksOutputData,
    IGetTasksPresenter,
)


class GetTasksGuiPresenter(IGetTasksPresenter):
    def format(self, output_data: GetTasksOutputData) -> dict:
        response = {}
        for task in output_data.tasks:
            response[task.id_] = {
                "description": task.description,
            }
        return response
