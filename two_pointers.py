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


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
