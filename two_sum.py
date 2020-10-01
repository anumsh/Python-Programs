# Given the list of numbers and a target, We have to find two numbers such that the addition of two numbers in the list should be equal to the target.
#Input: list of numbers, target
#Output: Index of two numbers
class Solution:
    def twoSum(self, nums, target):
        hash={}
        for i in range(len(nums)):
            com = target - nums[i]
            if com not in hash:
                hash[nums[i]]=i
            else:
                return [hash[com],i]

s1 = Solution()
nums = [2,7,11,15]
target = 9
print(s1.twoSum(nums , target ))