#User function Template for python3
a = int(input())
b = int(input())

# Your code here
while b != 0:
    a,b = b,a%b
print(a)
