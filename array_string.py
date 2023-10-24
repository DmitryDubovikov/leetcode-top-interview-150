class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        88. Merge Sorted Array
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[l] = nums1[m]
                m -= 1
            else:
                nums1[l] = nums2[n]
                n -= 1
            l -= 1

        while n >= 0:
            nums1[l] = nums2[n]
            n -= 1
            l -= 1

        # print(nums1)

    def removeElement(self, nums: list[int], val: int) -> int:
        """27. Remove Element"""
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

    def removeDuplicates(self, nums: list[int]) -> int:
        """26. Remove Duplicates from Sorted Array"""
        last_unique = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                last_unique += 1
                nums[last_unique] = nums[i]
        # print(nums)
        return last_unique + 1

    def majorityElement(self, nums: list[int]) -> int:
        """169. Majority Element"""
        freq = dict()
        half = len(nums) // 2

        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1

        for k, v in freq.items():
            if v > half:
                return k

        # print(freq)
        return 0

    def maxProfit(self, prices: list[int]) -> int:
        """121. Best Time to Buy and Sell Stock"""
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
            r += 1

        return max_profit

    def romanToInt(self, s: str) -> int:
        """13. Roman to Integer"""
        res = 0
        rv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(len(s) - 1):
            if rv[s[i]] < rv[s[i + 1]]:
                res -= rv[s[i]]
            else:
                res += rv[s[i]]

        return res + rv[s[-1]]


if __name__ == "__main__":
    s = Solution()
    # print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    # print(s.removeElement(nums=[3, 2, 2, 3], val=3))
    # print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    # print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
    # print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(s.romanToInt("MCMXCIV"))
