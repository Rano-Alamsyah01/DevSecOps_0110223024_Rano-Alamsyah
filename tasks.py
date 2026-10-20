from dataclasses import dataclass, asdict


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False

    def to_dict(self):
        return asdict(self)
