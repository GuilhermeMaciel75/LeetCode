nums = [2,1,5,0,4,6]
count = 0
idxCurrent = 0
idxSecond = 0
minNumber = nums[0]


while len(nums) >= 2:
    if idxCurrent >= len(nums):
        nums.pop(0)
        idxCurrent = 0
        count = 0
        idxSecond = 0
        minNumber = nums[0]

    elif count == 0 and nums[0] < nums[idxCurrent]:
        count += 1
        idxSecond = idxCurrent

    elif count == 1 and nums[idxSecond] < nums[idxCurrent]:
        count += 1

    elif count == 1 and nums[idxSecond] > nums[idxCurrent] and nums[idxCurrent] > nums[0]:
        idxSecond = idxCurrent

    if count >= 2:
        print(True)
    
    else:
        idxCurrent += 1


print(False)
"""minValue = nums.index(min(nums))
maxValue = nums.index(max(nums))


while len(nums) > 2:
    for x in range(len(nums)):

        if nums[x] > nums[minValue] and nums[x] < nums[maxValue] and x > minValue and x < maxValue:
            print(True)

    nums.pop(minValue)
    nums.pop(maxValue)
    minValue = nums.index(min(nums))
    maxValue = nums.index(max(nums))

print(False)"""