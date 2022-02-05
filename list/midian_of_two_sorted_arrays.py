#!/usr/bin/python
#encoding =utf-8
'''
level: hard
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
overall explanation: https://www.youtube.com/watch?v=LPFhl65R7ww
'''
def findMedianSortedArrays(nums1, nums2):
    if len(nums2) < len(nums1):
        return findMedianSortedArrays(nums2, nums1)

    n1, n2 = len(nums1), len(nums2)
    low, high = 0, n1

    while low <= high:
        #cut1 + cut2 = (n1+n2+1)/2 即切分满足两边的元素数量之和等于两个数组长度的一半
        cut1=(low + high) // 2
        cut2= (n1 + n2 + 1) // 2 - cut1

        l1= float("-inf") if cut1 == 0 else nums1[cut1-1]
        l2= float("-inf") if cut2 == 0 else nums2[cut2-1]
        r1= float("inf") if cut1 == n1 else nums1[cut1]
        r2= float("inf") if cut2 == n2 else nums2[cut2]
        #中位数刚好在两个数组的中间
        if l1 <= r2 and l2 <= r1:
            if((n1+n2) % 2 == 0):
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)
        #数组1中的元素比较大，即中位数在数组1的左边
        elif l1 > r2:
            high = cut1 - 1
        #数组2中的元素比较大，中位数在数据1的右边
        else:
            low = cut1 + 1
    return 0.0

if __name__ == '__main__':
    nums1 = [1,3,4]
    nums2 = [2]
    num3 = findMedianSortedArrays(nums1, nums2)
    print(f"the medium is : {num3}")
    #测试 float("-inf")是否是最小负数
    #if float("-inf") < -10000:
    #    print("-inf < -10000")
    #else:
    #    print("-inf >= -10000")
