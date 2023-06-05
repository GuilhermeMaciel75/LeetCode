class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maior = soma = sum(nums[0 : k])
        
        for i in range(len(nums) - k):
            soma += nums[i + k] - nums[i]

            if soma >= maior:
                maior = soma

        return maior / k
