#User function Template for python3
#Back-end complete function Template for Python 3
n = int(input())

########### Write your code below ###############
if n <=0:
    fib =0
elif n ==1:
    fib =1
elif n == 2:
    fib = 1
else:
    a,b =0,1
    for _ in range (2, n+1):
       a,b = b,a+b
    fib =b


########### Write your code above ###############
print(fib)
