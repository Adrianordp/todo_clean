"""
entity/task.py

Entity for task.
"""

from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class ITask(Protocol):
    """
    Interface for task.

    :param int id_: The id of the task.
    :param str description: The description of the task.
    """

    id_: int
    description: str


@dataclass
class Task(ITask):
    """Task class."""

    id_: int
    description: str
