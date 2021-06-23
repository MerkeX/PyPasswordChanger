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
    With the option (1) you insert the site name and your user name one by one
    (Boring and time consuming if you have a lot of passwords to change).
    
    - OPTION 2:
    With the option (2), you will need to have the exported file containing all of
    stored password (You can obtain it from 'passwords.google.com' or, if you're
    using Google Chrome, by typing "chrome://settings/passwords" in the address bar);
    Nonetheless, you have the possibility to actually encrypt your password, using a simple
    'Caesar Cipher', so you can write down your passwords without worrying about some one
    getting his hands on your them.
    
    - OPTION 3:
    Print this help message

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
        print("\n")
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
