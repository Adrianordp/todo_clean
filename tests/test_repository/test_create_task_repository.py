"""
Test CreateTaskSqliteRepository.
"""

import sqlite3
from contextlib import closing

import pytest

from todo_clean.layer3.repository.create_task_repository import (
    CreateTaskSqliteRepository,
)


@pytest.fixture(name="in_memory_db")
def fixture_in_memory_db():
    """
    Create an in-memory SQLite database

    :return sqlite3.Connection: The connection to the SQLite database."""
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


def test_create_task_sqlite_repository(in_memory_db):
    """
    Test CreateTaskSqliteRepository

    :param sqlite3.Connection in_memory_db: The connection to the SQLite
    database.
    """
    task_repo = CreateTaskSqliteRepository(in_memory_db)
    description1 = "Test task1"
    description2 = "Test task2"
    task1 = task_repo.create_task(description1)
    task2 = task_repo.create_task(description2)

    with closing(in_memory_db.cursor()) as cursor:
        cursor.execute("SELECT * FROM tasks")
        result = cursor.fetchall()

        assert result[0][0] == task1.id_
        assert result[0][1] == task1.description

        assert result[1][0] == task2.id_
        assert result[1][1] == task2.description
