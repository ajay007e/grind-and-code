class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.sl = SortedList()
        self.task_info = {}

        for u, t, p in tasks:
            self.sl.add((p, t, u))
            self.task_info[t] = (p, u)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.sl.add((priority, taskId, userId))
        self.task_info[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        old_p, u = self.task_info[taskId]
        self.sl.discard((old_p, taskId, u))
        self.sl.add((newPriority, taskId, u))
        self.task_info[taskId] = (newPriority, u)

    def rmv(self, taskId: int) -> None:
        old_p, u = self.task_info[taskId]
        self.sl.discard((old_p, taskId, u))
        del self.task_info[taskId]

    def execTop(self):
        if not self.sl:
            return -1
        old_p, old_t, u = self.sl[-1]
        self.sl.pop(-1)
        return u
        return task.userId
