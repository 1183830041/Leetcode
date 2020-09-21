#4. 罗马数字转整数
def romanToInt(self, s: str) -> int:
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}#利用字典表示字符所对应的数值
        ans = 0
        for i in range(len(s)):#获取字符串长度
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:#当不是最后一个字符，前一个字符小于后一个字符时当进行减法运算
                ans -= a[s[i]]
            else:
                ans += a[s[i]]#其他的进行加法运算
        return ans



#5. 最长公共前缀
def longestCommonPrefix(self, strs):
        if len(strs) == 0:#当strs为0时返回空
            return ""
        n = len(strs[0])#获取strs中第一个字符串的长度
        for e in strs:
            n = min(n, len(e))#比较获取strs中最短字符串的长度
        for i in range(0, n):
            for e in strs:
                if e[i] != strs[0][i]:#当字符串中的字符不相等时返回前面字符
                    return e[:i]
        return strs[0][:n]

#6.删除排序数组中的重复项
def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        b = 1
        while b < len(nums):
            if nums[a] == nums[b]:
                nums.pop(a) 
            else:
                a += 1
                b += 1
        return len(nums)