class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip_array = address.split('.')
        res = ""
        for ip in ip_array:
            if res is "":
                res = ip
            else:
                res += "[.]" + ip
        return res