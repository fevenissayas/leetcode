class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        for i, val in enumerate(s):
            if val.lower() in s and val.upper() in s:
                continue
            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i+1:])
            return (left if len(left) >= len(right) else right)
        return s