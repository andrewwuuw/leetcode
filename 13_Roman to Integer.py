class Solution:
    def romanToInt(self, s: str) -> int:
        r_list = list(s)
        roman_symbol = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if (len(r_list) == 1):
            return roman_symbol[r_list[0]]
        
        left, right = "", ""
        total, init = 0, 0
        
        for symbol in r_list:
            if (init==0):
                left = symbol
                init += 1
            elif (init==1):
                right = symbol
                init += 1
                total = self.calc_total(roman_symbol, left, right, total)
            else:
                left = right
                right = symbol
                total = self.calc_total(roman_symbol, left, right, total)
        
        return total + roman_symbol[right]

    def calc_total(self, roman_symbol: dict, left: str, right: str, total: int):
        if roman_symbol[left] >= roman_symbol[right]:
            return total + roman_symbol[left]
        elif roman_symbol[left] < roman_symbol[right]:
            return total - roman_symbol[left]
        
sol = Solution()
print(sol.romanToInt("MDMXIV"))
