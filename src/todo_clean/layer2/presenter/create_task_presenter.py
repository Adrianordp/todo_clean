"""
presenter/create_task_presenter.py

Presenter for creating task use case.
"""

from dataclasses import dataclass

from src.todo_clean.layer1.usecase.create_task import (
    CreateTaskResponse,
    ICreateTaskPresenter,
)


@dataclass
class CreaTaskViewModel:
    """ViewModel for creating task use case."""

    id: str
    description: str


class CreateTaskGuiPresenter(ICreateTaskPresenter):
    """GUI presenter for creating task use case."""

    view_model: CreaTaskViewModel

    def format(self, output_data: CreateTaskResponse) -> None:
        idoutput_data = CreaTaskViewModel(
            str(output_data.id_), output_data.description
        )
        CreateTaskGuiPresenter.view_model = idoutput_data
