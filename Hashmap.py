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
        return ms == mt

    def wordPattern(self, pattern: str, s: str) -> bool:
        """290. Word Pattern"""
        map_p = [pattern.index(ch) for ch in pattern]
        s_list = s.split(" ")
        map_s = [s_list.index(w) for w in s_list]
        return map_p == map_s

    def isAnagram(self, s: str, t: str) -> bool:
        """242. Valid Anagram"""
        from collections import defaultdict

        counter = defaultdict(int)

        for ch in s:
            counter[ch] += 1
        for ch in t:
            counter[ch] -= 1

        return all(v == 0 for v in counter.values())


if __name__ == "__main__":
    s = Solution()
    # print(s.canConstruct(ransomNote="aa", magazine="aab"))
    # print(s.isIsomorphic(s="bbbaaaba", t="aaabbbba"))
    # print(s.wordPattern(pattern="abba", s="dog cat cat dog"))
    print(s.isAnagram(s="anagram", t="nagaram"))
