import functools

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nlist = list(map(int, str(n)))
        return functools.reduce(lambda x, y: x*y, nlist) - functools.reduce(lambda x, y: x+y, nlist)
