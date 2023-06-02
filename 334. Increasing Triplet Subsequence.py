nums = [2,1,5,0,4,6]

orderList = nums.copy()
orderList.sort()

for i in range(len(nums)-2):
    if nums.index(orderList[i]) < nums.index(orderList[i+1]) and nums.index(orderList[i+1]) < nums.index(orderList[i+2]):
        print(True)
print(False)
