from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class ITask(Protocol):
    id_: int
    description: str


@dataclass
class Task(ITask):
    id_: int
    description: str
    # title: str
    # status: str
