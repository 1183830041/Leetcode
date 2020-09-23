#1最长公共前缀
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