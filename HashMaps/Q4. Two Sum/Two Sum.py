class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
#created  map with idx values of nums elements
#fixing the first no. then searching for the second no. in the map
#if sec no. found in map then pushed idx of elements in result vector
