class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        while s[index] == " ":
            index -= 1
        
        wordLength = 0

        while s[index] != " " and index >= 0:
            wordLength += 1
            index -=1
        
        return wordLength