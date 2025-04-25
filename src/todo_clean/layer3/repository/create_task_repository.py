"""
Implementation of ICreateTaskRepository.
"""

import sqlite3
from contextlib import closing

from todo_clean.layer0.entity.task import ITask, Task
from todo_clean.layer1.usecase.create_task import ICreateTaskRepository


class CreateTaskSqliteRepository(ICreateTaskRepository):
    """
    Implementation of ICreateTaskRepository for SQLite.

    :param sqlite3.Connection conn: The connection to the SQLite database.
    """

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_task(self, description: str) -> ITask:
        self._create_table()
        with closing(self.conn.cursor()) as cursor:
            cursor.execute(
                "INSERT INTO tasks (description) VALUES (?)", (description,)
            )
            self.conn.commit()
            return Task(cursor.lastrowid, description)

    def _create_table(self):
        with closing(self.conn.cursor()) as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL
                )
            """
            )
            self.conn.commit()
