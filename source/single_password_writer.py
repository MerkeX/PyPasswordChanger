# file: single_password_writer.py
#
# INSERT NAME OF SITE, USER AND PASSWORD SETTINGS EVERYTIME
#
import os,sys,platform
from getpass import getuser
import caesar_cipher,password_generator
from tkinter.filedialog import askdirectory
from tkinter import Tk
Tk().withdraw();

charset_0 = "abcdefghijklmnopqrstuvwxyz0123456789";
charset_1 = charset_0 + "@#$%&";
charset_2 = charset_0 + "ABCDEGHIJKLMNOPQRSTUVWXYZ";
charset_3 = charset_2 + "@#$%&";

def execute():
    # LET USER SELECT THE FOLDER IN WHICH STORE THE FILE(S)
    # IF THE LOCATION IS INCORRECT OR WE CAN'T ACCESS IT,
    # USE THE 'DESKTOP' FOLDER
    print(">> Select path for password list: \n");
    try:
        path = askdirectory();
        # SELECTED NO FOLDER, USING DESKTOP AS WORKING DIRECTORY
        if(path == ""):
            print(">> No folder selected. File(s) will be stored in Desktop");
            current_username = getuser();
            if(os.name == "nt"):
                path =  "C:\\Users\\" + current_username + "\\Desktop";
            elif(os.name == "posix"):
                path = "/home/" + current_username + "/";
        # SELECTED VALID FOLDER, ADDING SEPARATOR
        if(os.name == "nt"):
            path = path + "/";
        elif(os.name == "posix"):
            path = path + "/";
    # SOME ERRORS OCCURRED, USING DESKTOP AS WORKING DIRECTORY
    except:
        current_username = getuser();
        if(os.name == "nt"):
            path =  "C:\\Users\\" + current_username + "\\Desktop";
        elif(os.name == "posix"):
            path = "/home/" + current_username + "/";
    print(">> Files will be created in ",path);

    # CHECK IF THE FILES ARE ALREADY THERE
    # IF SO, WE DELETE THEM

    pass_text_num = str(input(">> Would you like to write passwords and encrypted password in the same file?[y/n]: "));
    if(pass_text_num == 'y' or pass_text_num == 'Y'):
        if (os.path.isfile(path + "list_passwords_and_encrypted.csv") == 'True'):
            os.remove(path + "list_passwords_and_encrypted.csv");
        num_files = 1;
    elif(pass_text_num == 'n' or pass_text_num == 'N'):
        if (os.path.isfile(path + "list_clear_passwords_new.csv") == 'True'):
            os.remove(path + "list_clear_passwords_new.csv");
        if (os.path.isfile(path + 'list_encrypted_passwords_new.csv') == 'True'):
            os.remove(path + 'list_encrypted_passwords_new.csv');
        num_files = 2;
    else:
        print(">> Choice not valid. Two files will be created");
        if (os.path.isfile(path + "list_clear_passwords_new.csv") == 'True'):
            os.remove(path + "list_clear_passwords_new.csv");
        if (os.path.isfile(path + 'list_encrypted_passwords_new.csv') == 'True'):
            os.remove(path + 'list_encrypted_passwords_new.csv');
        num_files = 2;
    # EXECUTION WITH TWO FILES
    if(num_files == 2):
        flag = 0;
        clear_password_file = open(path + "list_clear_password.csv","w");
        encrypt_password_file = open(path + "list_encrypt_password.csv","w");
        clear_header = "SITE;USERNAME;PASSWORD\n";
        encrypt_header = "SITE;USERNAME;ENCRYPTED PASSWORD\n";
        clear_password_file.write(clear_header);
        encrypt_password_file.write(encrypt_header);
        while(flag == 0):
            site_name = str(input(">> Insert site: "));
            # site_name[0] == " " --> USER CAN INSERT ANY NUMBER OF SPACES
            # 'site_name' IS ALWAYS INVALID; JUST CHECK THE FIRST CHAR
            while(site_name == "" or site_name[0] == " "):
                print(">> 'Site' can't be empty. Retry");
                site_name = str(input(">> Insert site: "));
            user_name = str(input(">> Insert username: "));
            # user_name[0] == " " --> SAME AS 'user_name'
            while(user_name == "" or user_name[0] == " "):
                print(">> 'username' can't be empty. Retry");
                user_name = str(input(">> Insert username: "));
            print(">> Generating password...\n");
            print(">> Charset available: ");
            print(">> 1 - ",charset_0);
            print(">> 2 - ",charset_1);
            print(">> 3 - ",charset_2);
            print(">> 4 - ",charset_3);
            selection = str(input(">> Select charset [1-4]: "));
            if(selection == '1'):
                charset = charset_0;
            elif(selection == '2'):
                charset = charset_1;
            elif(selection == '3'):
                charset = charset_2;
            elif (selection == '4'):
                charset = charset_3;
            else:
                print(">> Invalid choice. Default (1) will be used");
                charset = charset_0;
            try:
                length_password = int(input(">> Set password length [6-128]: "));
                if(length_password > 128):
                    print(">> Maximum password length reached. Length password will be 128");
                    length_password = 128;
                if(length_password < 6):
                    print(">> Minimum password length not reached. Length password will be 6");
                    length_password = 6;

            # IF THERE'S ANY ERROR (NEGATIVE NUMBER, LETTERS) JUST PUT A LENGTH OF 16
            except:
                print(">> Incorrect input. Length is set to 16");
                length_password = 16;
            password = password_generator.create_password(length_password,charset);
            caesar_password = caesar_cipher.execute(password);
            delimiter = ";";
            clear_password_file.write(site_name + delimiter + user_name + delimiter + password + "\n");
            encrypt_password_file.write(site_name + delimiter + user_name  + delimiter + caesar_password + "\n");

            ans = str(input(">> Repeat?[Y/n] "));
            if(ans == 'y' or ans == 'Y'):
                flag = 0;
            else:
                flag = 1; # WE'RE DONE
                clear_password_file.close();
                encrypt_password_file.close();
        print(">> Program Terminated!\n");
    # EXECUTION WITH ONLY ONE FILE
    else:
        flag = 0;
        clear_encrypt_password_file = open(path + "list_clear_encrypt_password.csv","w");
        header = "SITE;USERNAME;PASSWORD;ENCRYPTED PASSWORD\n";
        clear_encrypt_password_file.write(header);
        while(flag == 0):
            site_name = str(input(">> Insert site: "));
            # site_name[0] == " " --> USER CAN INSERT ANY NUMBER OF SPACES
            # 'site_name' IS ALWAYS INVALID; JUST CHECK THE FIRST CHAR
            while(site_name == "" or site_name[0] == " "):
                print(">> 'Site' can't be empty. Retry");
                site_name = str(input(">> Insert site: "));
            user_name = str(input(">> Insert username: "));
            # user_name[0] == " " --> SAME AS 'user_name'
            while(user_name == "" or user_name[0] == " "):
                print(">> 'username' can't be empty. Retry");
                user_name = str(input(">> Insert username: "));
            print(">> Generating password...\n");
            print(">> Charset available: ");
            print(">> 1 - ",charset_0);
            print(">> 2 - ",charset_1);
            print(">> 3 - ",charset_2);
            print(">> 4 - ",charset_3);
            selection = str(input(">> Select charset [1-4]: "));
            if(selection == '1'):
                charset = charset_0;
            elif(selection == '2'):
                charset = charset_1;
            elif(selection == '3'):
                charset = charset_2;
            elif (selection == '4'):
                charset = charset_3;
            else:
                print(">> Invalid choice. Default (1) will be used");
                charset = charset_0;
            try:
                length_password = int(input(">> Set password length: "));
                if(length_password > 128):
                    print(">> Maximum password length reached. Length password will be 128");
                    length_password = 128;
            # IF THERE'S ANY ERROR (NEGATIVE NUMBER, LETTERS) JUST PUT A LENGTH OF 16
            except:
                print(">> Incorrect input. Length is set to 16");
                length_password = 16;
            password = password_generator.create_password(length_password,charset);
            caesar_password = caesar_cipher.execute(password);
            delimiter = ";";
            clear_encrypt_password_file.write(site_name + delimiter + user_name + delimiter + password + delimiter + caesar_password +"\n");
            ans = str(input(">> Repeat?[Y/n] "));
            if(ans == 'y' or ans == 'Y'):
                flag = 0;
            else:
                clear_encrypt_password_file.close();
                flag = 1; #WE'RE DONE
        print(">> Program Terminated!\n");
