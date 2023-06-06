class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maior, maiorSegundo = inf, inf

        for n in nums: 
            if n <= maior: 
                maior = n

            elif n <= maiorSegundo:
                maiorSegundo = n

            else:
                return True

        return False
