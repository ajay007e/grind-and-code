class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            vi = int(v1[i])
            vj = int(v2[j])
            if vi < vj:
                return -1
            elif vi > vj:
                return 1
            else:
                i += 1
                j += 1
        while i < len(v1):
            if int(v1[i]) > 0:
                return 1
            else:
                i += 1
        while j < len(v2):
            if int(v2[j]) > 0:
                return -1
            else:
                j += 1
        return 0
