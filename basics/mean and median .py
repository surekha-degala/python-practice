class Solution:
    def median(self, arr):
        #code here
        n = len(arr)
        arrr = sorted(arr)
        mid = n //2
        if (n %2 == 0):
            return (arrr[mid-1]+ arrr[mid])//2
        else:
            return arrr[mid]
        
    
    def mean(self, arr):
        #code here
        return sum(arr)//len(arr)
