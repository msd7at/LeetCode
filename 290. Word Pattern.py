class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = dict()
        str_list = str.split()
        if(len(pattern) != len(str_list)):
            return False
        for i in range(len(pattern)):
            if(pattern[i] in d):
                if(str_list[i] != d[pattern[i]]):
                    return False
                   
            if(pattern[i] not in d):
                if(str_list[i] in d.values()):
                    return False
                d[pattern[i]] = str_list[i]
                   
        return True
