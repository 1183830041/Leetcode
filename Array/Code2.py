#2.移除元素
def removeElement(nums,val):
    val = int(val)
    j=0
    for i in range(len(nums)):
        if val!=nums[i]:
            nums[j]=nums[i]
            j+=1
    print(nums)
    return j