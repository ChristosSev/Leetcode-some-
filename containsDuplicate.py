def containsDuplicate(nums):

    numSet = set()
    for i in range(0,len(nums)):
        while nums[i] not in numSet:
            numSet.add(nums[i])
            #print(len(numSet))
    print(len(numSet))
    if len(numSet) == len(nums):
            return False
    else:
            return True
