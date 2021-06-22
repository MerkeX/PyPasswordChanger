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
                elif(stayInAlphabet < ord('A')):
                    stayInAlphabet += 26
                finalLetter = chr(stayInAlphabet)
                cipherText += finalLetter
            elif(char.islower() == True):
                stayInAlphabet = ord(char) + shift
                if(stayInAlphabet > ord('z')):
                    stayInAlphabet -= 26
                elif(stayInAlphabet < ord('a')):
                    stayInAlphabet += 26
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
    
    def IncreasingCaesar(self,plainText,shift):
        """
        It's like Caesar(plainText,shift), but the shift
        increases by 1 every step (that's why "Increasing")
        Example:
            plainText = abcdefgh
            Caesar(plainText,2) = cdefghij
            IncreasingCaesar(plainText,2) = cegikmoq
        """
        cipherText = ""; i = 0
        for char in plainText:
            cipherChar = self.Caesar(char,(shift + i))
            cipherText += cipherChar
            i += 1
        self.cipherText = cipherText

    def DecreasingCaesar(self,plainText,shift):
        """
        It's like Caesar(plainText,shift), but the shift
        decreases by 1 every step (that's why "Decreasing")
        Example:
            plainText = abcdefgh
            Caesar(plainText,2) = cdefghij
            DecreasingCaesar(plainText,2) = cbazyxwv
        """
        cipherText = ""; i = 0
        for char in plainText:
            cipherChar = self.Caesar(char,(shift - 2*i))
            cipherText += cipherChar
            i += 1
        self.cipherText = cipherText