# Question 1 count_evens
def count_evens(nums):
  total = 0  
  for x in nums : 
    if x%2 == 0:
      total = total + 1 
  return total


# Question 2 big_diff
def big_diff(nums):  
  dif = 0
  mi=min(nums)
  ma=max(nums)
  dif = ma - mi
  return dif


# Question 3 centered_average 
def centered_average(nums):
  ave  = 0
  ma = max(nums)
  nums.remove(ma)
  mi = min(nums)
  nums.remove(mi)
  ave = sum(nums)/len(nums)
  return ave


# Question 4 sum13 
def sum13(nums):
  total = 0
  for i in range(len(nums)):
    x = nums[i]
    if nums[i -1] == 13 and i != 0:
      pass
    elif x == 13:
      total = total + 0
    else:
      total = total + x
  return total


# Question 5 sum67 
def sum67(nums):
  for i in range(len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)


# Question 6 has22 
def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False
  

