#2. 整数反转
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            x = int('-' + s[1:][::-1])
        else:
            x = int(s[::-1])
        if x >= 2147483647 or x <= -2147483648: # 判断溢出情况
            return 0
        return x
