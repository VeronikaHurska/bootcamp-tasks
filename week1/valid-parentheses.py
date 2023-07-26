class Solution(object):
    def isValid(s):
        stack = []
        bracket_map = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in bracket_map.keys():
                stack.append(char)
            elif char in bracket_map.values():
                if not stack or bracket_map[stack.pop()] != char:
                    return False
            else:
                return False
        return not stack


print(Solution.isValid(")"))
