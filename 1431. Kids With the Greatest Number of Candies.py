class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        result = []

        for n in candies:
            result.append(n + extraCandies >= maxCandy)

        return result