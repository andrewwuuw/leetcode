class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 1:
            return strs[0]

        minimum, init = 0, 0
        main_list = []
        res = ""
        
        for i in strs:
            if i == "":
                return ""
            sub_list = []
            minimum = self.get_minimum(minimum, len(i))
            for j in i:
                sub_list.append(j)
            main_list.append(sub_list)
        
        check = True
        for j in range(0, minimum):
            for i in range(0, len(main_list)):
                if i+1 != len(main_list):
                    if main_list[i][j] != main_list[i+1][j]:
                        check = False
            if check:
                res = res + main_list[0][j]
        return res
            

    def get_minimum(self, left=0, right=0):
        if left == 0:
            left = right
            return left
        elif left <= right:
            return left
        elif left > right:
            return right
        
r_list = ["flower", "flow", "flight"]
sol = Solution()
print(sol.longestCommonPrefix(r_list))
