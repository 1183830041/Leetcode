#1.爬楼梯
def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(3,n+1):
            t = b
            b = a + b
            a = t
        return b