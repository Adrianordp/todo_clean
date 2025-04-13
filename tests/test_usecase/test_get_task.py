from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_task import GetTaskById, GetTaskByIdInputData


def test_get_task():

    class TaskRepoSpy(ITaskRepo):
        id_: int
        task: Task

        def new_task(self, description: str) -> Task:
            pass

        def get_task_by_id(self, id_: int) -> Task:
            self.id_ = id_
            self.task = Task(self.id_, "Random Task")
            return self.task

        def get_tasks(self) -> list[Task]:
            pass

        def edit_task_by_id(self, id_: int) -> Task:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            pass

    task_repo_spy = TaskRepoSpy()
    target_id = 1
    input_data = GetTaskByIdInputData(target_id)
    usecase = GetTaskById(task_repo_spy)
    output_data = usecase.execute(input_data)
    assert output_data.task.id_ == target_id
    assert output_data.task == task_repo_spy.task
