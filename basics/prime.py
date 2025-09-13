#User function Template for python3
n = int(input())
is_prime = True
# Your code here
for i in range (2,n):
    if n%i== 0:
        is_prime = False
        break
if is_prime and n >1:
    print("True")
else:
    print("False")




