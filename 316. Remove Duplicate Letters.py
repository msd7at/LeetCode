#  https://leetcode.com/problems/remove-duplicate-letters/
class Solution:
    def removeDuplicateLetters(self, text: str) -> str:
        s=collections.Counter(text)
        stack,visited=[],set()
        for i in text:
            s[i]-=1
            if i not in visited:
                while stack and stack[-1] > i and s[stack[-1]]>0:
                    visited.remove(stack.pop())
                visited.add(i)
                stack.append(i)
        return "".join(stack)
