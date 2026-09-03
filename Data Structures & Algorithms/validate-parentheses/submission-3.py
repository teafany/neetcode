class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stk = []
        for char in s:
            if char in pairs:
                if stk and stk[-1] == pairs[char]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(char)
        return True if not stk else False




