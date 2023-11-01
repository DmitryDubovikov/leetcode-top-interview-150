class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """3. Longest Substring Without Repeating Characters"""
        max_len = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(s="abcabcbb"))
