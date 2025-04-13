from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.usecase.create_task import ICreateTaskPresenter


class CreateTaskGuiPresenter(ICreateTaskPresenter):
    def format(self, output_data: ITask) -> dict:
        return {"id": output_data.id_, "description": output_data.description}
