def isPalindrome(s):
    #code here
    s = s.strip().lower()
    i , j = 0, len(s)-1
    while (i<j):
        if s[i]!= s[j]:
            return False
        i +=1
        j -=1
    return True
            
    def isPalindrome(s):
    s = s.strip()               # optional: remove leading/trailing whitespace
    return s.lower() == s[::-1].lower()

