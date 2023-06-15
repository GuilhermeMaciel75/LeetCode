class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        altitude = 0

        for n in range(len(gain)):
            altitude +=  gain[n]
            if altitude > max:
                max = altitude

        return max