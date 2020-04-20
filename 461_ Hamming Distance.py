class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_list = self.get_binary_list(x)
        y_list = self.get_binary_list(y)
        x_list, y_list = self.add_zero(x_list, y_list)

        n = 0
        for i in range(0, len(x_list)):
            if x_list[i] != y_list[i]:
                n += 1
        return n

    def get_binary_list(self, x):
        r_list = []
        while x != 0:
            r_list.insert(0, x%2)
            x //= 2
        return r_list
    
    def add_zero(self, x=[], y=[]):
        distance = abs(len(x)-len(y))
        for i in range(0, distance):
            if len(x) > len(y):
                y.insert(0, 0)
            elif len(x) < len(y):
                x.insert(0, 0)
        return x, y

sol = Solution()
print(sol.hammingDistance(123, 12351641614))