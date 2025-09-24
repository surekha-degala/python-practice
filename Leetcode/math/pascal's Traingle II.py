class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        li = []
        val =1
        for k in range(rowIndex+1):
            li.append(val)
            val = val * (rowIndex -k)//(k+1)
        return li
