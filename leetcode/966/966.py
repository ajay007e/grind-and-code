class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        perfect = set(wordlist)
        cap = {}
        vow = {}

        for word in wordlist:
            low = word.lower()
            if low not in cap:
                cap[low] = word
            devow = self.devowel(low)
            if devow not in vow:
                vow[devow] = word

        ans = []
        for query in queries:
            if query in perfect:
                ans.append(query)
                continue

            low = query.lower()
            if low in cap:
                ans.append(cap[low])
                continue

            devow = self.devowel(low)
            if devow in vow:
                ans.append(vow[devow])
                continue

            ans.append("")
        return ans

    def devowel(self, word):
        return "".join("*" if c in "aeiou" else c for c in word)
