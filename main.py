from typing import List

def twoSum(nums: List[int], target:int)->List[int]:
    output = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
                return output
    return output

    