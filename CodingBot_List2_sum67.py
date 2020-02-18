#sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])

def sum67(nums):
  total = 0
  check = 0 
  
  for i in range(len(nums)):
    if nums[i] == 6:
      total = total + 0
      check = i
    elif nums[check] != 6 and nums[i] == 7:
      total = total + nums[i]
    elif nums[check] == 6 and nums[i] == 7:
      total = total + 0
    else:
      total = total + nums[i]
  return total


    # total = 0
    # found6 = False
      
    # for i in range(len(nums)):
    #     if nums[i] == 6:
    #         found6 = True
    #     if not found6:
    #         total += nums[i]
    #     if nums[i] == 7 and found6:
    #         found6 = False
            
    # return total
