from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.delete_task_by_id import (
    DeleteTask,
    DeleteTaskInputData,
    DeleteTaskOutputData,
)


def test_usecase_delete_task_by_id():

    class TaskRepoSpy(ITaskRepo):
        id_: int

        def create_task(self, description: str) -> ITask:
            pass

        def get_task_by_id(self, id_: int) -> ITask:
            pass

        def get_tasks(self) -> list[ITask]:
            pass

        def edit_task_by_id(self, id_: int) -> ITask:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            self.id_ = id_
            return True

    id_ = 1
    input_data = DeleteTaskInputData(id_)
    task_repo = TaskRepoSpy()
    usecase = DeleteTask(task_repo)
    output_data = usecase.execute(input_data)

    assert isinstance(output_data, DeleteTaskOutputData)
    assert output_data.success == True
