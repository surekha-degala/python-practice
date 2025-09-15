def reverseString(s):
    #code here
    rev = ""
    for i in s:
        rev = i + rev
    return rev
    
#built in operation
s = "abcd"
print(s[::-1])
