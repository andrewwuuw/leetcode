class Solution:
    def isPalindrome(self, x: int) -> bool:
        r_list = []
        for i in str(x):
            r_list.append(i)

        r_list_len = len(r_list)
        return self.loop_list_to_judge(r_list, 0, r_list_len-1)

    def loop_list_to_judge(self, list=[], head=0, footer=0):
        if (head == footer):
            return True

        if (head > 0) or (footer > 0):
            if (footer-head != 1) and (footer != head):
                if (list[head] == list[footer]):
                    return self.loop_list_to_judge(list, head+1, footer-1)
                else:
                    return False
            else:
                return (list[head] == list[footer])

sol = Solution()
print(sol.isPalindrome(100001))
