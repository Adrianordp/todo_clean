"""Implementation of IGetTasksRepository."""

import sqlite3
from contextlib import closing

from todo_clean.layer0.entity.task import ITask, Task
from todo_clean.layer1.usecase.get_tasks import IGetTasksRepository


class GetTasksSqliteRepository(IGetTasksRepository):
    """Implementation of IGetTasksRepository for SQLite."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_tasks(self) -> list[tuple[int, ITask]]:
        """Get tasks from SQLite repository."""
        with closing(self.conn.cursor()) as cursor:
            cursor.execute("SELECT id, description FROM tasks")
            return [Task(row[1]) for row in cursor.fetchall()]
