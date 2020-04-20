class Solution:
    def insertion_sort(self, lists= []) -> list:
        for i in range(1, len(lists)):
            key = lists[i]
            j = i-1
            while j >= 0 and key < lists[j]:
                lists[j+1] = lists[j]
                j -= 1
            lists[j+1] = key
        return lists
    
r_list = [32, 13, 34, 63, 91, 87, 89]
sol = Solution()
print(sol.insertion_sort(r_list))