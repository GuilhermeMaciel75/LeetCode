#Resolution using set

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]
     
#Resolution whitout set

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = []
        list2 = []

        for n1 in nums1:
            if n1 not in nums2 and n1 not in list1:
                list1.append(n1)

        for n2 in nums2:
            if n2 not in nums1  and n2 not in list2:
                list2.append(n2)


        return [list1, list2]
