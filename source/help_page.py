#
# HELP PAGE
#
# print_help_guide() JUST PRINTS WHAT IS WRITTEN IN THE FILE 'HELP.txt'
# LOCATED IN THE SAME FOLDER; IT IS MADE JUST FOR EASE; IT IS SIMPLER
# TO MODIFY A TEXT FILE

import os,sys

def print_help_guide():
    #path = os.path.dirname(os.path.abspath(__file__));
    path = os.getcwd();
    if(os.name == "nt"):
        path = path + "\\";
    elif(os.name == "posix"):
        path = path + "/";
    try:
        help_file = open(path + "HELP.txt");
        while(1):
            line = help_file.readline();
            if(line == ""):
                break;
            if(line[0] == '#'):
                print(" ");
            else:
                print(line)
    except:
        print(">> ERROR. File 'HELP.txt' not found\n")

    print(">> Select an option");
    print(">>");
    print(">> 1 - Execute the program");
    print(">> 2 - Update the password");
    print(">> X - Exit the program");
    print("\n");

    op = str(input(">> "));

    if(op == str(1)):
        Password.Single();

    elif(op == str(2)):
        Password.Update();

    elif(op == str('x') or op == str('x')):
        print(">> You chose to close this tool. Exiting...")
        sys.exit(0);

    else:
        print(">> Program terminated without harming the system!\n");
        sys.exit(0);
