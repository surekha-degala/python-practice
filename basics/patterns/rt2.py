class Solution:
    def printPattern(self, n):
        #Code here
        for i in range (1,n+1):
            if i ==1:
                print("*")
            elif i == n:
                print("* "*n)
            else:
                print("*"+" "*(2*(i-1)-1)+"*")
                
                
                
                
                
                
                
