#1.删除排序数组中的重复项
def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums)==0:
        return 0
    temp = []
    temp.append(nums[0])#写入列表中的第一个元素
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:#后一个元素和前一个元素进行比较不等就写入
            temp.append(nums[i])
    nums[:]=temp#覆盖列表
    return len(nums)