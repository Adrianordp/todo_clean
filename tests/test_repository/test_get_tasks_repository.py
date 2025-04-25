"""
Test GetTasksSqliteRepository.
"""

import sqlite3
from contextlib import closing

import pytest

from todo_clean.layer3.repository.get_tasks_repository import (
    GetTasksSqliteRepository,
)


@pytest.fixture(name="tasks")
def fixture_tasks() -> list[dict[str, int | str]]:
    """
    Fixture for tasks.

    :return list[dict[str, int | str]]: The list of tasks.
    """
    return [
        {"id": 1, "description": "Test task 1"},
        {"id": 2, "description": "Test task 2"},
    ]


@pytest.fixture(name="in_memory_db")
def fixture_in_memory_db(tasks: list[dict[str, int | str]]):
    """
    Create an in-memory SQLite database

    :param list[dict[str, int | str]] tasks: The list of tasks

    :return sqlite3.Connection: The connection to the SQLite database.
    """
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
            "INSERT INTO tasks (description) VALUES (?)",
            (tasks[0]["description"],),
        )

        conn.commit()

        cursor.execute(
            "INSERT INTO tasks (description) VALUES (?)",
            (tasks[1]["description"],),
        )

        conn.commit()
    yield conn
    conn.close()


def test_create_task_sqlite_repository(
    in_memory_db: sqlite3.Connection, tasks: list[dict[str, int | str]]
):
    """
    Test CreateTaskSqliteRepository

    :param sqlite3.Connection in_memory_db: The connection to the SQLite
    database.
    :param list[dict[str, int | str]] tasks: The list of tasks
    """

    repository = GetTasksSqliteRepository(in_memory_db)
    repository.get_tasks()

    with closing(in_memory_db.cursor()) as cursor:
        cursor.execute("SELECT * FROM tasks")
        result = cursor.fetchall()

        assert len(result) == 2
        assert result[0][1] == tasks[0]["description"]
        assert result[1][1] == tasks[1]["description"]
        assert result == [
            (tasks[0]["id"], tasks[0]["description"]),
            (tasks[1]["id"], tasks[1]["description"]),
        ]
