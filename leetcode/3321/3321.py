class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n, res = len(nums), []
        fm = defaultdict(int)
        top, low = SortedList(), SortedList()
        curr = 0

        def change(num, count):
            nonlocal curr

            prev = (fm[num], num)
            if fm[num]:
                if prev in low:
                    low.discard(prev)
                else:
                    top.discard(prev)
                    curr -= fm[num] * num
            fm[num] += count

            if fm[num]:
                low.add((fm[num], num))

            while low and len(top) < x:
                freq, key = low.pop(-1)
                curr += freq * key
                top.add((freq, key))

            while low and low[-1] > top[0]:
                freq, key = low.pop(-1)
                xfreq, xkey = top.pop(0)
                curr = curr - xfreq * xkey + freq * key
                low.add((xfreq, xkey))
                top.add((freq, key))

        for i in range(n):
            change(nums[i], 1)
            if i >= k:
                change(nums[i - k], -1)
            if i >= k - 1:
                res.append(curr)
        return res
