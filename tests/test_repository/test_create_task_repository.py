import sqlite3
from contextlib import closing

import pytest

from src.todo_clean.layer0.entity.task import Task
from src.todo_clean.layer1.repository.create_task_repository import (
    CreateTaskSqliteRepository,
)


@pytest.fixture(name="in_memory_db")
def fixture_in_memory_db():
    """Create an in-memory SQLite database"""
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


def test_create_task_sqlite_repository(in_memory_db):
    """Test CreateTaskSqliteRepository"""
    task_repo = CreateTaskSqliteRepository(in_memory_db)
    description = "Test task"
    task = Task(1, description)
    task_repo.create_task(description)

    with closing(in_memory_db.cursor()) as cursor:
        cursor.execute("SELECT * FROM tasks")
        result = cursor.fetchone()

        assert result[0] == task.id_
        assert result[1] == task.description
