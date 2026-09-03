class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stk = []
        for char in s:
            if char in pairs.values():
                stk.append(char)
            if char in pairs.keys():
                if stk and stk[-1] == pairs[char]:
                    stk.pop()
                else:
                    return False
        return True if not stk else False




