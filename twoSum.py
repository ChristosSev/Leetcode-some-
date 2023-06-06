def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate((nums)):
        comp = target-num
    
        if comp in hashmap:
            return [hashmap[comp],i]
        else:
            hashmap[num] = i
    return []
