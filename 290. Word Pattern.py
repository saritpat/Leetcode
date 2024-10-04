class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        dict2 = {}

        s = s.split(' ')

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dict:
                dict[pattern[i]] = s[i]
            
            else:
                if dict[pattern[i]] != s[i]:
                    return False
            
            if s[i] not in dict2:
                dict2[s[i]] = pattern[i]

            else:
                if dict2[s[i]] != pattern[i]:
                    return False

        return True

S = Solution()
pattern = "abc"
s = "b c a"
print(S.wordPattern(pattern, s))