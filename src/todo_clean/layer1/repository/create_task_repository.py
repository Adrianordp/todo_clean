"""Implementation of ICreateTaskRepository."""

import sqlite3
from contextlib import closing

from src.todo_clean.layer0.entity.task import ITask
from src.todo_clean.layer1.usecase.create_task import ICreateTaskRepository


class CreateTaskSqliteRepository(ICreateTaskRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_task(self, description: str) -> int:
        self._create_table()
        with closing(self.conn.cursor()) as cursor:
            cursor.execute(
                "INSERT INTO tasks (description) VALUES (?)", (description,)
            )
            self.conn.commit()
            return cursor.lastrowid

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
