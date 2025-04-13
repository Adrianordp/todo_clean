from src.todo_clean.layer1.usecase.delete_task_by_id import (
    IDeleteTaskByIdPresenter,
)


class DeleteTaskByIdGuiPresenter(IDeleteTaskByIdPresenter):
    def format(self, output_data: bool) -> None:
        return {"success": output_data}
