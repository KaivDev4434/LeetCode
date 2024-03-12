"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


def merge_array(num1, m, num2, n):
    if n == 0:
        return
    del num1[m:]
    num1.extend(num2)
    # print(num1)
    num1.sort()
    print(num1)


merge_array([1], 1, [], 0)
