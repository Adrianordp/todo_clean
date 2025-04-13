from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.usecase.get_task_by_id import IGetTaskByIdPresenter


class GetTaskByIdGuiPresenter(IGetTaskByIdPresenter):
    def format(self, output_data: ITask) -> dict:
        return {"id": output_data.id_, "description": output_data.description}
