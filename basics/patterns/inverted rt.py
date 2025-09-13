class Solution:
    def printPattern(self, n):
        #Code here
        
        for i in range(n,0,-1):
            print("* "*i)


#User function Template for python3
n = int(input())

# Your code here
for i in range(n,0,-1):
    for j in range(i):
        print("* ", end = "")
    print()
            
            
