"""
presenter/create_task_presenter.py

Presenter for creating task use case.
"""

from todo_clean.layer1.usecase.create_task import (
    CreaTaskViewModel,
    CreateTaskResponse,
    ICreateTaskPresenter,
)


class CreateTaskGuiPresenter(ICreateTaskPresenter):
    """GUI presenter for creating task use case."""

    view_model: CreaTaskViewModel

    def format(self, output_data: CreateTaskResponse) -> None:
        idoutput_data = CreaTaskViewModel(
            output_data.id_, output_data.description
        )
        CreateTaskGuiPresenter.view_model = idoutput_data
