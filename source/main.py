#!/usr/bin/env python

# Author:  MerkeX
#
# Date:    28/11/2018
#

import os,sys,platform,getpass
import single_password_writer,password_generator,help_page,password_list_generator,password_updater

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
print(">> 3 - Update the passwords --> Update a previous passwords list");
print(">> 4 - Print the help page  --> Get some help with this tool");
print(">> X - Exit the program\n");

op = str(input(">> "));

if(op == str(1)):
    single_password_writer.execute();

elif(op == str(2)):
    password_list_generator.execute();

elif(op == str(3)):
    password_updater.execute();

elif(op == str(4)):
    help_page.print_help_guide();
    
elif(op == str('X') or op == str('x')):
    print(">> Closing the program as requested...");
    sys.exit(0);
else:
    # INPUT WAS INVALID. EXIT
    print(">> Program terminated without harming the system!\n");
    sys.exit(0);
