from tasks import Task


class TaskStore:
    """Penyimpanan in-memory untuk demonstrasi; data hilang saat proses berhenti."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def list_tasks(self):
        return [task.to_dict() for task in self._tasks]

    def add_task(self, title):
        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task.to_dict()

    def delete_task(self, task_id):
        for index, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[index]
                return True
        return False
