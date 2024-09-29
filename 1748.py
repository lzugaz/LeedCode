from typing import List
def sumOfUnique( nums: List[int]) -> int:
    freq = {}
    for item in nums:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    sum = 0
    for key, value in freq.items():
        if value == 1:
            sum += key
    return sum


nums = [1,2,2,2,4,5,6]
print(sumOfUnique(nums))

