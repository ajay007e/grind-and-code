class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            res.append(n)

            while len(res) > 1:
                n1, n2 = res[-2], res[-1]
                g = gcd(n1, n2)
                if g == 1:
                    break
                res.pop()
                res[-1] = n1 * n2 // g

        return res
