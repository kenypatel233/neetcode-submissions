class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                hmap={}
                for i,value in enumerate(nums):
                    difference = target - value
                    if difference in hmap:
                         return [hmap[difference], i]
                    else:
                        hmap[value]=i

        