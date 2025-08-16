class Solution:
    def maximum69Number(self, num: int) -> int:
        res = str(num)
        for i in range(len(res)):
            if res[i] == "6":
                res = res[:i] + "9" + res[i + 1 :]
                return int(res)
        return int(res)
