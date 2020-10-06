#8.多数元素
def majorityElement(nums):#摩尔投票法
        major = 0
        count = 0
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1
        return major

if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    tag = majorityElement(nums)
    print(tag)
