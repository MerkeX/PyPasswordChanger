
import string

class Cipher:
    
    def __init__(self, cipherText):
        self.cipherText = cipherText
        
    def Caesar(self,plainText,shift):
        """Insert text to encode and shift"""
        cipherText = ""
        for char in plainText:
            if(char.isupper() == True):
                stayInAlphabet = ord(char) + shift
                if(stayInAlphabet > ord('Z')):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                cipherText += finalLetter
            elif(char.islower() == True):
                stayInAlphabet = ord(char) + shift
                if(stayInAlphabet > ord('z')):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                cipherText += finalLetter
            elif(char.isdigit() == True):
                digit = int(char)
                finalNumber = ((digit + shift) % 10)
                cipherText = cipherText + str(finalNumber)
            else:
                # if the char is nor a letter nor a digit
                # just copy it (special characters, spaces, etc.)
                cipherText = cipherText + str(char)
            
            self.cipherText = cipherText
            
    def ProgressiveCaesar(self,plainText,shift):
        l = len(plainText) - 1
        cipherText = ""
        for i in range(0,l):
            char = plainText[i]
            cipherChar = self.C
        