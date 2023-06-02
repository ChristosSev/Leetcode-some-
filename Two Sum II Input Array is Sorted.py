def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1


    while l<r:
          sum = (numbers[l] + numbers[r])
          print(sum )
          if sum == target:
              return [l+1, r+1]
          elif sum  < target:
               l+=1

          elif sum  > target:
               r -=1



    return
