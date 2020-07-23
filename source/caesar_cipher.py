
# In general, this function should be 'def caesar(plainText, shift):
# We set a costant shift of 2

import string

def execute(plainText):
  shift = 2;
  cipherText = "";
  for char in plainText:
    if(char.isupper() == True):
      stayInAlphabet = ord(char) + shift;
      if(stayInAlphabet > ord('Z')):
          stayInAlphabet -= 26;
      finalLetter = chr(stayInAlphabet);
      cipherText += finalLetter;
    elif(char.islower() == True):
      stayInAlphabet = ord(char) + shift;
      if(stayInAlphabet > ord('z')):
        stayInAlphabet -= 26;
      finalLetter = chr(stayInAlphabet);
      cipherText += finalLetter;
    elif(char.isdigit() == True):
        digit = int(char);
        finalNumber = ((digit + shift) % 10);
        cipherText = cipherText + str(finalNumber);
    else:
        # if the char is nor a letter nor a digit,
        # just copy it (special characters, etc..)
        cipherText = cipherText + str(char);
  return cipherText;
