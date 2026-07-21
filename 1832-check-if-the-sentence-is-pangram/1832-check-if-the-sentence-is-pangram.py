class Solution(object):
    def checkIfPangram(self, sentence):
        alph = "abcdefghijklmnopqrstuvwxyz"
        
        for char in alph:
            if char  not in sentence:
                return False
        return True

        