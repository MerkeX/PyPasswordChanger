#!/usr/bin/env python

# Author:  MerkeX
#
# Date:    28/11/2018
#

import os,sys,platform,getpass
import Password

def main():
    # START HEADER
    print("\n");

    print("========== PASSWORD CHANGER ===========\n");
    if(os.name == "nt"):
        print(">> OS Detected: " + str(platform.system()) + " " + str(platform.release()) + " " + "v" + str(platform.version())[5:]);
    elif(os.name == "posix"):
        print(">> OS Detected: " + str(platform.system()) + " " + str(platform.release()));

    # END HEADER

    print("\n");
    # OPERATION SELECTION
    print(">> Welcome! Please press:");
    print(">> 1 - Execute the program  --> Generate password one by one");
    print(">> 2 - Automated process    --> Get input file and write all passwords");
    print(">> 3 - Print the help page  --> Get some help with this tool");
    print(">> X - Exit the program\n");

    op = str(input(">> "));

    if(op == str(1)):
        Password.Single();

    elif(op == str(2)):
        Password.Update();

    elif(op == str(3)):
        help_page.print_help_guide();

    elif(op == str('X') or op == str('x')):
        print(">> Closing the program as requested...");
        sys.exit(0);
    else:
        # INPUT WAS INVALID. EXIT
        print(">> Program terminated without harming the system!\n");
        sys.exit(0);

if __name__ == '__main__':
    main();
