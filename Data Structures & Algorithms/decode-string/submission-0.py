class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=0
        currStr=""

        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=='[':
                stack.append((currStr,num))
                currStr=""
                num=0
            elif ch=="]":
                prevStr,repeat=stack.pop()
                currStr = prevStr+ currStr*repeat
            else:
                currStr +=ch

        return currStr
