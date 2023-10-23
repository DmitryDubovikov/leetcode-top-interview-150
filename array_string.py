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

        print(nums1)


if __name__ == "__main__":
    s = Solution()
    print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
