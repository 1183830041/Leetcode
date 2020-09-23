#2. 罗马数字转整数
def romanToInt(self, s: str) -> int:
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}#利用字典表示字符所对应的数值
        ans = 0
        for i in range(len(s)):#获取字符串长度
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:#当不是最后一个字符，前一个字符小于后一个字符时当进行减法运算
                ans -= a[s[i]]
            else:
                ans += a[s[i]]#其他的进行加法运算
        return ans