class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = [
            ("(", ")"),
            ("[", "]"),
            ("{", "}")
        ]

        r_list = []
        for i in s:
            r_list.append(i)
        if len(r_list)%2 != 0:
            return False
        return self.check_valid(parentheses, r_list, 0, len(r_list)-1)

    def check_valid(self, parentheses=[], list=[], head=0, footer=0):
        if footer-head != -1:
            self.check_valid(list, head+1, footer-1)
            for j in range(0, len(parentheses)):
                if list[head] == parentheses[j][0]:
                    if list[footer] == parentheses[j][1]:
                        return True

sol = Solution()
print(sol.isValid("{}"))
