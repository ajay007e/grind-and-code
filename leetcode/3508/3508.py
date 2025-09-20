class Router:
    def __init__(self, memoryLimit: int):
        self.mx = memoryLimit
        self.all = deque()
        self.unique = set()
        self.dest_t = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.unique:
            return False

        if len(self.all) == self.mx:
            s, d, t = self.all.popleft()
            self.unique.remove((s, d, t))
            self.dest_t[d].popleft()

        self.all.append(key)
        self.unique.add(key)
        self.dest_t[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.all:
            return []
        s, d, t = self.all.popleft()
        self.unique.remove((s, d, t))
        self.dest_t[d].popleft()
        return s, d, t

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.dest_t[destination]
        l = bisect_left(arr, startTime)
        r = bisect_right(arr, endTime)
        return r - l
