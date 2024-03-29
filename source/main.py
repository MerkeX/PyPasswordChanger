#!/usr/bin/env python

# Author:  MerkeX
#
# Date:    28/11/2018
#

import os,sys,platform
import passwd

def main():
    """
    HELP PAGE
    This tool allows you to generate new passwords for all your websites account.
    
    - OPTION 1:
    With the option (1) you insert the site name and your user name one by one,
    choosing every time the charset and the length of your passwords in case you 
    never save your passwords on your browsers or you have never used a password manager. 
    (Boring and time consuming if you have a lot of passwords to add).
    You also have the possibility to write a file with your passwords encrypted with a 
    'Caesar cipher' (a simple shift of the letters through the alphabet), in case you
    want to print or store your passwords on your pc without having them in clear text.
    
    - OPTION 2:
    With the option (2), you will need to have the exported file containing all of
    stored passwords, from a browser or a password manager (must be in a .csv format).
    From this file, 'Group', 'Site name' and 'user name' field will be obtained, followed 
    by a new fresh generated password (you must choose the charset and the length of the passwords).
    Like the option (1), you have the possibility to write a file with your password encrypted, to
    keep it on your pc, or print it as well.
    
    - OPTION 3:
    Print this help message.
    
    ****                                                                             ****
    ** If you want to test the software, to check how it works without using your real **
    ** usernames and passwords, you can use the test file in the 'example' folder.     **
    ****                                                                             ****

    /END
    """
    print("\n")
    # OPERATION SELECTION
    print(":: 1 - Generator")
    print(":: 2 - Updater")
    print(":: 3 - Help")
    print(":: X - Exit the program\n")

    op = str(input(">> "))
    if(op == str(1)):
        Passwd = passwd.Password("","",0)
        Passwd.Single()

    elif(op == str(2)):
        Passwd = passwd.Password("","",0)
        Passwd.Update()

    elif(op == str(3)):
        print(main.__doc__)
        main()

    elif(op == str('X') or op == str('x')):
        print(":: Closing the program as requested...")
        sys.exit(0)
    else:
        # INPUT WAS INVALID. EXIT
        print(":: Program terminated without harming the system!\n")
        sys.exit(0)
        
if __name__ == '__main__':
    # START HEADER
    print("\n")
    print("========== PASSWORD CHANGER ===========\n");
    if(os.name == "nt"):
        print(":: OS Detected: " + str(platform.system()) + " " + str(platform.release()) + " " + "v" + str(platform.version())[5:])
    elif(os.name == "posix"):
        print(":: OS Detected: " + str(platform.system()) + " " + str(platform.release()))

    # END HEADER
    print(":: Welcome! Please press:")
    main()
