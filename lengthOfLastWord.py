class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if all(ch.isalpha() or ch == " " for ch in s):
        #     len_lastword  = len(s.strip().split(" ")[-1])
        #     return len_lastword
        # else:
        #     return False

        len_lastword  = len(s.strip().split(" ")[-1])
        return len_lastword



solution = Solution()
print(solution.lengthOfLastWord("i   am  on the     moon        "))