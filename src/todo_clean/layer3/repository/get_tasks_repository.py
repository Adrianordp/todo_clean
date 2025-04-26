"""
Implementation of IGetTasksRepository for SQLite.
"""

import sqlite3
from contextlib import closing

from todo_clean.layer0.entity.task import ITask, Task
from todo_clean.layer1.usecase.get_tasks import IGetTasksRepository


class GetTasksSqliteRepository(IGetTasksRepository):
    """
    Implementation of IGetTasksRepository for SQLite.

    :param sqlite3.Connection conn: The connection to the SQLite database.
    """

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_tasks(self) -> list[ITask]:
        with closing(self.conn.cursor()) as cursor:
            try:
                cursor.execute("SELECT id, description FROM tasks")
            except sqlite3.OperationalError:
                return []
            return [Task(row[0], row[1]) for row in cursor.fetchall()]
