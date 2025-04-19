# from todo_clean.layer0.entity.task import ITask
# from todo_clean.layer1.repository.i_task_repo import ITaskRepo
# from todo_clean.layer1.usecase.get_task_by_id import (
#     GetTaskById,
#     GetTaskByIdInputData,
#     GetTaskByIdOutputData,
#     IGetTaskByIdPresenter,
# )


# def test_get_task():

#     class TaskRepoSpy(ITaskRepo):
#         get_task_by_id_called = False
#         get_task_by_id_called_with = {}

#         def create_task(self, description: str) -> ITask:
#             pass

#         def get_task_by_id(self, id_: int) -> ITask:
#             self.get_task_by_id_called = True
#             self.get_task_by_id_called_with["id"] = id_

#         def get_tasks(self) -> list[ITask]:
#             pass

#         def edit_task_by_id(self, id_: int) -> ITask:
#             pass

#         def delete_task_by_id(self, id_: int) -> bool:
#             pass

#     class GetTaskByIdPresenterSpy(IGetTaskByIdPresenter):
#         format_called = False
#         format_called_with = {}

#         def format(self, output_data: GetTaskByIdOutputData) -> None:
#             self.format_called = True
#             self.format_called_with["output_data"] = output_data

#     id_ = 1
#     input_data = GetTaskByIdInputData(id_)

#     task_repo_spy = TaskRepoSpy()
#     presenter_spy = GetTaskByIdPresenterSpy()

#     usecase = GetTaskById(task_repo_spy, presenter_spy)
#     usecase.execute(input_data)

#     assert task_repo_spy.get_task_by_id_called is True
#     assert task_repo_spy.get_task_by_id_called_with["id"] == id_

#     assert presenter_spy.format_called is True
#     assert presenter_spy.format_called_with["output_data"] is not None
#     assert isinstance(
#         presenter_spy.format_called_with["output_data"], GetTaskByIdOutputData
#     )
