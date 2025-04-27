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
            select_query = "SELECT * FROM tasks WHERE id = ?"
            delete_query = "DELETE FROM tasks WHERE id = ?"
            try:
                if cursor.execute(select_query, (id_,)).fetchone() is None:
                    return False
                cursor.execute(delete_query, (id_,))
                self.conn.commit()
            except sqlite3.OperationalError:
                return False
            except sqlite3.InterfaceError:
                return False
        return True
