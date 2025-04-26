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

    def format(self, response: CreateTaskResponse) -> None:
        idoutput_data = CreaTaskViewModel(response.id_, response.description)
        CreateTaskGuiPresenter.view_model = idoutput_data
