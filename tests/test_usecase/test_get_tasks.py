from src.todo_clean.layer0.entity.task import ITask, Task
from src.todo_clean.layer1.repository.i_task_repo import ITaskRepo
from src.todo_clean.layer1.usecase.get_tasks import GetTasks, GetTasksOutputData


def test_get_tasks():

    class TaskRepoSpy(ITaskRepo):
        task1 = Task(1, "Random task 1")
        task2 = Task(2, "Random task 2")
        task_list = [task1, task2]

        def create_task(self, description: str) -> ITask:
            pass

        def get_task_by_id(self, id_: int) -> ITask:
            pass

        def get_tasks(self) -> list[ITask]:
            return self.task_list

        def edit_task_by_id(self, id_: int) -> ITask:
            pass

        def delete_task_by_id(self, id_: int) -> bool:
            pass

    task_repo = TaskRepoSpy()
    usecase = GetTasks(task_repo)
    output_data = usecase.execute()

    assert isinstance(output_data, GetTasksOutputData)
    assert output_data.tasks == task_repo.task_list
