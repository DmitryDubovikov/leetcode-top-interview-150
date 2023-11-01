class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        rc = Counter(ransomNote)
        mc = Counter(magazine)

        # print(rc, mc, rc & mc)

        return rc & mc == rc

    def isIsomorphic(self, s: str, t: str) -> bool:
        """205. Isomorphic Strings"""

        ms = []
        mt = []
        for ch in s:
            ms.append(s.index(ch))
        for ch in t:
            mt.append(t.index(ch))
        # print(ms, mt)
        ms = [s.index(ch) for ch in s]
        return ms == mt


if __name__ == "__main__":
    s = Solution()
    # print(s.canConstruct(ransomNote="aa", magazine="aab"))
    print(s.isIsomorphic(s="bbbaaaba", t="aaabbbba"))
