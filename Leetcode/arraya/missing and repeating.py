class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        rep = -1
        total = n * (n+1) // 2
        sum_a = 0
        
        seen = set()
        for num in arr:
            if num in seen: 
                rep = num
            else:
                seen.add(num)
            sum_a += num
        missing = total - (sum_a - rep)
        return [rep, missing]

