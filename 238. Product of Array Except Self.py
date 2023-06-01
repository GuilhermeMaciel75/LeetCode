class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lenght = len(nums)
        finalList = [0] * lenght
        total = 1
        zero = False
        for i in nums:
            if i != 0:
                total *= i
            elif i == 0 and zero:
                total = 0
            else:
                zero = True

        for j in range(lenght):
            if nums[j] != 0 and zero:
                finalList[j] = (0)

            elif nums[j] != 0:
                finalList[j] = (int(total / nums[j]))
            else:
                finalList[j] = (total)

        return finalList