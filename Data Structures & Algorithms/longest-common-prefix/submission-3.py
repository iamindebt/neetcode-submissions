class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strings = sorted(strs, key=len)
        shared = True
        for index, l in enumerate(strings[0]):
            pre = strings[0][0:index+1]
            print(pre)
            for s in strings:
                if pre not in s:
                    shared = False
            if shared:
                prefix = pre

        return prefix
        

