#3.搜索插入位置
def searchInsert(self, nums: List[int], target: int) -> int:
        position = 0 # 位置变量
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                #mark += 1
                if target > nums[i]:
                    position += 1
        return position