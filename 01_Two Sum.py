class Solution:
    def twoSum(self, nums: list, target: int):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
r_list = [1, 6, 3, 5]
sol = Solution()
print(sol.twoSum(r_list, 11))