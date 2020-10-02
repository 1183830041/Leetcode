#3.两数之和 II - 输入有序数组
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for x in range(n):
            a = target - numbers[x]
            if a in numbers:
                y = numbers.index(a)
                if x == y:
                    continue
                else:
                    return  min(x+1,y+1),max(x+1,y+1)
            else:
                continue