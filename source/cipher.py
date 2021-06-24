class Cipher:
    
    def __init__(self, cipherText):
        self.cipherText = cipherText
        
    def Caesar(self,plainText,shift):
        """Insert text to encode and shift"""
        cipherText = ""
        
        # A shift of 32 (example) is useless
        # shift is meant to be [1-25]
        if(shift > 26):
            shift = (shift % 26)
        for char in plainText:
            if(char.isupper() == True):
                new_ord = ord(char) + shift
                if(new_ord > ord('Z')):
                    new_ord -= 26
                elif(new_ord < ord('A')):
                    new_ord += 26
                finalLetter = chr(new_ord)
                cipherText += finalLetter
            elif(char.islower() == True):
                new_ord = ord(char) + shift
                if(new_ord > ord('z')):
                    new_ord -= 26
                elif(new_ord < ord('a')):
                    new_ord += 26
                finalLetter = chr(new_ord)
                cipherText += finalLetter
            elif(char.isdigit() == True):
                digit = int(char)
                finalNumber = ((digit + shift) % 10)
                cipherText = cipherText + str(finalNumber)
            else:
                # if the char is nor a letter nor a digit
                # just copy it (special characters, spaces, etc.)
                cipherText = cipherText + str(char)
        return cipherText
    
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