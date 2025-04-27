"""
Implementation of IDeleteTaskByIdRepository.
"""

import sqlite3
from contextlib import closing

from todo_clean.layer1 import IDeleteTaskByIdRepository


class DeleteTaskByIdSqliteRepository(IDeleteTaskByIdRepository):
    """
    Implementation of IDeleteTaskByIdRepository for SQLite.

    :param sqlite3.Connection conn: The connection to the SQLite database.
    """

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def delete_task_by_id(self, id_: int) -> bool:
        with closing(self.conn.cursor()) as cursor:
            if (
                cursor.execute(
                    "SELECT * FROM tasks WHERE id = ?", (id_,)
                ).fetchone()
                is None
            ):
                return False
            try:
                cursor.execute("DELETE FROM tasks WHERE id = ?", (id_,))
                self.conn.commit()
            except sqlite3.OperationalError:
                return False
            except sqlite3.InterfaceError:
                return False
        return True
