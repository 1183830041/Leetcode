#7.只出现一次的数字
def singleNumber(self, nums: List[int]) -> int:
        nums.sort()#先对数组排序
        n=len(nums)
        for i in range(0,n,2):#取索引值每次间隔为2
            if i+1<n:
                if nums[i]!=nums[i+1]:
                    return nums[i]
            else:
                return nums[i]
