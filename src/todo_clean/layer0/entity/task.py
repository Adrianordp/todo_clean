"""
entity/task.py

Entity for task.
"""

from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class ITask(Protocol):
    """Interface for task."""

    description: str


@dataclass
class Task(ITask):
    """Task class."""

    description: str
