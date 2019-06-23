class Solution:
    def convert_nagative(self, is_nagative: bool, x: int):
        if is_nagative:
            return -x
        else:
            return x
    
    def is_int32(self, x:int):
        if x<pow(2,31) and x>=-pow(2,31):    
            return x
        else:
            return 0

    def reverse(self, x: int) -> int:
        is_negative = False
        r_list=[]
        res=""
        if x<0:
            is_negative = True
            x = abs(x)
        for i in str(x):
            r_list.append(i)
        for j in range(len(r_list)-1, -1, -1):
            res += str(r_list[j])
        return self.is_int32(self.convert_nagative(is_negative, int(res)))

sol = Solution()
sol.reverse(1238781273591213521352512387812735912135213525123878127359121352135251238781273591213521352512387812735912135213525123878127359121352135251238781273591213521352512387812735912135213525123878127359121352135251238781273591213521352512387812735912135213525)