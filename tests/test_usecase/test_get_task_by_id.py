from src.todo_clean.layer0.entity.task import ITask, Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_task_by_id import (
    GetTaskById,
    GetTaskByIdInputData,
    GetTaskByIdOutputData,
)


def test_get_task():

    class TaskRepoSpy(ITaskRepo):
        id_: int
        task: ITask

        def create_task(self, description: str) -> ITask:
            pass

        def get_task_by_id(self, id_: int) -> ITask:
            self.id_ = id_
            self.task = Task(self.id_, "Random task")
            return self.task

        def get_tasks(self) -> list[ITask]:
            pass

        def edit_task_by_id(self, id_: int) -> ITask:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            pass

    task_repo_spy = TaskRepoSpy()
    target_id = 1
    input_data = GetTaskByIdInputData(target_id)
    usecase = GetTaskById(task_repo_spy)
    output_data = usecase.execute(input_data)

    assert isinstance(output_data, GetTaskByIdOutputData)
    assert task_repo_spy.id_ == target_id
    assert output_data.task.id_ == target_id
