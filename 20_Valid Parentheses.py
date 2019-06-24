class Solution(object):
    def isValid(self, s):
        parenttheses = ["()", "[]", "{}"]
        while parenttheses[0] in s or parenttheses[1] in s or parenttheses[2] in s:
            s = s.replace(parenttheses[0], "").replace(parenttheses[1], "").replace(parenttheses[2], "")
        return s == ''

sol = Solution()
print(sol.isValid("{}[{}[]()()(]()"))