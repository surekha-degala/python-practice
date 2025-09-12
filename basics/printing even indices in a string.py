class Solution:
    def print_even_indices(self, s: str):
        #code here
        result = ""
        for i in range(0,len(s),2):
            result +=s[i]
        print(result)
                
