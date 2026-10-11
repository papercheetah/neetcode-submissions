class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        
        if len(nums) == 1:
            return nums[0]
            
        nums_dict = {}
        majority = len(nums) // 2

        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 0
            else:
                nums_dict[nums[i]] += 1
                if nums_dict.get(nums[i]) >= majority:
                    return nums[i]     
        
    