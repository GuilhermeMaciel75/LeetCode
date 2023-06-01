class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nPlots = 0
        lenArray = len(flowerbed)
        if lenArray > 1:

            for i in range(0, lenArray):

                if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    nPlots += 1
                    flowerbed[i] = 1

                elif i == (lenArray - 1) and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    nPlots += 1
                    flowerbed[i] = 1

                elif flowerbed[i] == 0 and  flowerbed[i - 1] == 0 and flowerbed[i+1] == 0:
                    nPlots += 1
                    flowerbed[i] = 1

        else:
            if flowerbed[0] == 0:
                 nPlots += 1

        return nPlots == n or nPlots >  n