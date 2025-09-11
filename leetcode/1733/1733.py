class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        non_native_friends = set()
        languages = [set(l) for l in languages]

        for a, b in friendships:
            a -= 1
            b -= 1
            if languages[a] & languages[b]:
                continue
            non_native_friends.add(a)
            non_native_friends.add(b)

        fm = defaultdict(int)
        for friend in non_native_friends:
            for l in languages[friend]:
                fm[l] += 1

        return len(non_native_friends) - max(fm.values() or [0])
