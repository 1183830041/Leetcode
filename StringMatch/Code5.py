#5.Excel表列名称
def convertToTitle(self, n: int) -> str:
        if n<=0: 
            return None 
        res = ''
        while n // 26 > 0:
            res = chr((n-1)%26 + 65) + res
            n = (n-1) // 26
        if n != 0:
            res = chr(n-1 + 65) + res
        return res