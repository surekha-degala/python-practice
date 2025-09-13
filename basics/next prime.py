#User function Template for python3

def nextPrime(n):
    
    # code here to find next prime number
    # return next prime number
    n = n+1
    while True:
        for i in range(2,n):
            if n%i == 0:
                break
        else:
                return n
        n+=1
