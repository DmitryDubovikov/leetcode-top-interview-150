class Solution:
    def isPalindrome(self, s: str) -> bool:
        """125. Valid Palindrome"""
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        """392. Is Subsequence"""
        if s == "":
            return True
        i = 0
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """167. Two Sum II - Input Array Is Sorted"""
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return []


if __name__ == "__main__":
    s = Solution()
    # print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
    # print(s.isSubsequence(s="abc", t="ahbgdc"))
    # print(s.isSubsequence(s="axc", t="ahbgdc"))
    print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
