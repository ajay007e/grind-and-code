class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisines_info = defaultdict(SortedList)
        self.food_info = {}

        for i in range(len(foods)):
            self.cuisines_info[cuisines[i]].add((-ratings[i], foods[i]))
            self.food_info[foods[i]] = (-ratings[i], cuisines[i])

    def changeRating(self, food: str, newRating: int) -> None:
        old_r, c = self.food_info[food]
        self.food_info[food] = (-newRating, c)
        self.cuisines_info[c].discard((old_r, food))
        self.cuisines_info[c].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_info[cuisine][0][1]

