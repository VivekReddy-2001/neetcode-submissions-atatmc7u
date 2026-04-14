class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoOpen={"]":"[","}":"{",")":"("}

        for c in s:
            if c in closetoOpen:
                if stack and stack[-1]==closetoOpen[c]:
                    stack.pop()#pop if we find matching
                else:# if we find close loop before open loop
                    return False
            else:
                stack.append(c) #append if we find opening loop
        return True if not stack else False