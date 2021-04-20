class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a=set()
        for i in sentence:
            a.add(i.lower())
        return len(a)==26
