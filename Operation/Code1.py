#1. 两数之和
class Solution:
	def twoSum(self,nums,target):
		n = len(nums)
		for x in range(n):
			a = target - nums[x]
			if a in nums: # 判断a有没有在nums数组里
				y = nums.index(a) # 有的话，那么用index获取到该数字的下标
				if x == y: 
					continue # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
				else: # 否则就返回结果
					return x,y 
					break
			else: 
				continue