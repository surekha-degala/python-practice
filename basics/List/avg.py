#User function Template for python3

def nonNegativeAverage(arr):
    
    #Write your code to find average of positive numbers in number list
    #Return the answer
    neg = [num for num in arr if num >=0]
    if not neg:
        return 0.0
    total = sum (neg)
    avg = total / len (neg)
    return avg
    
