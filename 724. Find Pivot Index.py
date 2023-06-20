class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft = 0
        sumRight = sum(nums)

        for x in range(0, len(nums)):
            sumRight -= nums[x]
            if sumleft == sumRight:
                return x

            sumleft += nums[x]

        return -1
