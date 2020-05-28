class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jsp = list(J)
        ssp = list(S)
        count = 0
        for i in jsp:
            count += ssp.count(i)
        return count
