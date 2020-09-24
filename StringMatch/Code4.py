#4.最后一个单词的长度
def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        str1 = []
        for i in range(0,len(s)):
            if s[i] == ' ':
                str1.append(s[0:i])
        str2 = []
        for i in range(0,len(s)):
            if s[i] == ' ':
                str2.append(s[i+1:len(s)])
        index = []
        for i in range(0,len(s)):
            if s[i] == ' ':
                index.append(i)
        str3 = []
        for i in range(0,len(s)):
            if s[i] == ' ':
                str3.append(str1[0])
                break
        for i in range(0,len(index)):
            if i < len(index)-1:
                str3.append(s[index[i] + 1:index[i+1]])
        for i in range(0,len(s)):
            if s[i] == ' ':
                str3.append(str2[len(str2)-1])
                break
        index1 = []
        for i in s:
            if i == ' ':
                index1.append(i)
        if len(index1) == 0:
            str3.append(s)
        return len(str3[len(str3)-1])