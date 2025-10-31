class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        found = set()
        for num in nums:
            if num in found:
                res.append(num)
            else:
                found.add(num)
        return res
