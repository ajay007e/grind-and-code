class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedList)
        self.sm_p = {}
        self.rented = SortedList()

        for s, m, p in entries:
            self.movies[m].add((p, s))
            self.sm_p[(s, m)] = p

    def search(self, movie: int) -> List[int]:
        res = []
        n = len(self.movies[movie])
        for i in range(5):
            if i == n:
                break
            res.append(self.movies[movie][i][1])
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.sm_p[(shop, movie)]
        self.movies[movie].discard((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.sm_p[(shop, movie)]
        self.movies[movie].add((price, shop))
        self.rented.discard((price, shop, movie))

    def report(self) -> List[List[int]]:
        res = []
        n = len(self.rented)
        for i in range(5):
            if i == n:
                break
            res.append((self.rented[i][1], self.rented[i][2]))
        return res
