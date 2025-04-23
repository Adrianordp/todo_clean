"""Test GetTasksSqliteRepository."""

import sqlite3
from contextlib import closing

import pytest

from todo_clean.layer3.repository.get_tasks_repository import (
    GetTasksSqliteRepository,
)


@pytest.fixture(name="in_memory_db")
def fixture_in_memory_db():
    """Create an in-memory SQLite database"""
    conn = sqlite3.connect(":memory:")
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
        """
        )
        conn.commit()

        cursor.execute(
            "INSERT INTO tasks (description) VALUES (?)", ("Test task 1",)
        )

        conn.commit()

        cursor.execute(
            "INSERT INTO tasks (description) VALUES (?)", ("Test task 2",)
        )

        conn.commit()
    yield conn
    conn.close()


def test_create_task_sqlite_repository(in_memory_db):
    """Test CreateTaskSqliteRepository"""

    repository = GetTasksSqliteRepository(in_memory_db)
    repository.get_tasks()

    with closing(in_memory_db.cursor()) as cursor:
        cursor.execute("SELECT * FROM tasks")
        result = cursor.fetchall()

        assert len(result) == 2
        assert result[0][1] == "Test task 1"
        assert result[1][1] == "Test task 2"
        assert result == [(1, "Test task 1"), (2, "Test task 2")]
