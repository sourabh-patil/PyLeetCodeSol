"""
Question:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs_dict = {')':'(','}':'{',']':'['}

        stack = []

        i = 0

        while len(stack) != 0 or i < len(s):
            if i == len(s) and len(stack) != 0:
                return False 
            if s[i] in pairs_dict.values(): ## opening bracket
                stack.append(s[i])
                i += 1
            elif s[i] in pairs_dict.keys(): ## closing bracket
                if len(stack) == 0:
                    return False
                popped_item = stack.pop()
                if popped_item != pairs_dict[s[i]]:
                    return False
                else:
                    i += 1

        return True 

        