class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomc = Counter(ransomNote)
        magazinec = Counter(magazine)
        for char ,count in  ransomc.items():
            if magazinec[char] <count:
                return False
        return True

        
