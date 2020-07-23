
# file: password_list_generator.py

import os,sys,platform,csv
from getpass import getuser
import password_generator,caesar_cipher
from tkinter.filedialog import askdirectory, askopenfilename
# WE HAVE TO DRAW A TK ROOT WINDOW BECAUSE IF WE DON'T DO THAT,
# A NEW ONE WILL BE OPENED WHEN ASKING FOR THE FILE
from tkinter import Tk
Tk().withdraw();
from pathlib import Path

charset_0 = "abcdefghijklmnopqrstuvwxyz0123456789";
charset_1 = charset_0 + "@#$%&";
charset_2 = charset_0 + "ABCDEGHIJKLMNOPQRSTUVWXYZ";
charset_3 = charset_2 + "@#$%&";

def execute():
    #CHARSET SELECTION
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
    # LENGTH SELECTION
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
    # FILE SECTION
    pass_text_num = str(input(">> Would you like to write passwords and encrypted password in the same file?[y/n]: "));
    print(">> Select the file exported from your browser:\n ");
    try:
        path_plus_filename = askopenfilename();
        while(Path(path_plus_filename).suffix != '.csv'):
            print(">> File selected is not a csv. Retry...");
            path_plus_filename = askopenfilename();
        path = os.path.dirname(path_plus_filename);
        filename = os.path.basename(path_plus_filename);
        if(os.name == "nt"):
            path = path + "\\";
        elif(os.name == "posix"):
            path = path + "/";
        # IF NOTHING IS SELECTED, WE CAN'T ACCESS THE FOLDER OR ANYTHING ELSE
        # PUT THE FILES ON THE DESKTOP
    except:
        print(">> No file selected. Program will now exit");
        sys.exit(0);
    print(">> File(s) will be created in " + path);

    # CHECK IF THE FILES ARE ALREADY THERE
    # IF SO, WE DELETE THEM

    if(pass_text_num == 'y' or pass_text_num == 'Y'):
        if (os.path.isfile(path + "list_clear_and_encrypted_passwords.csv") == 'True'):
            os.remove(path + "list_clear_and_encrypted_passwords.csv");
        num_files = 1;
    elif(pass_text_num == 'n' or pass_text_num == 'N'):
        if (os.path.isfile(path + "list_clear_passwords_new.csv") == 'True'):
            os.remove(path + "list_clear_passwords_new.csv");
        if (os.path.isfile(path + 'list_encrypted_passwords_new.csv') == 'True'):
            os.remove(path + 'list_encrypted_passwords_new.csv');
        num_files = 2;
    else: # INVALID CHOICE --> CHOOSE TO USE 2 FILE
        print(">> Choice not valid. Two files will be created");
        if (os.path.isfile(path + "list_clear_passwords_new.csv") == 'True'):
            os.remove(path + "list_clear_passwords_new.csv");
        if (os.path.isfile(path + 'list_encrypted_passwords_new.csv') == 'True'):
            os.remove(path + 'list_encrypted_passwords_new.csv');
        num_files = 2;

    # EXECUTION WITH ONLY ONE FILE
    if(num_files == 1):
        with open(path + 'list_clear_and_encrypted_passwords.csv',mode = 'w',newline = "\n") as list_clear_encrypted_passwords:
            clear_encrypted_writer = csv.writer(list_clear_encrypted_passwords,delimiter = ";")
            clear_encrypted_writer.writerow(["SITE","USERNAME","PASSWORD","ENCRYPTED PASSWORD"]);
            with open(path_plus_filename,mode = 'r') as chrome_exported_passwords:
                for i,row in enumerate(chrome_exported_passwords.readlines()):
                    if(i == 0): # SKIP 'SITE','USERNAME',[...], ROW
                        pass;
                    else:
                        try:
                            items = row.split(',');
                            site_name = items[0];
                            user_name = items[1];
                            password = password_generator.create_password(length_password, charset);
                            caesar_password = caesar_cipher.execute(password);
                            clear_encrypted_writer.writerow([site_name,user_name,password,caesar_password,]);
                        except:
                            items = row.split(';');
                            site_name = items[0];
                            user_name = items[1];
                            password = password_generator.create_password(length_password, charset);
                            caesar_password = caesar_cipher.execute(password);
                            clear_encrypted_writer.writerow([site_name,user_name,password,caesar_password,]);
    # EXECUTION WITH TWO FILES
    else:
        #
        # NOTE:
        # I had to write the file with the clear passwords and after that the one
        # with the encrypted password because .csv files can't be processed as
        # normal text file (as far as I know);
        # So, I'll write the first file, and then use it to create the second
        #

        # NOW WE CREATE THE NEW FILE CONTAINING ALL THE NEW (CLEAR) PASSWORDS
        with open(path + 'list_clear_passwords.csv',mode = 'w',newline = "\n") as list_clear_passwords:
            clear_writer = csv.writer(list_clear_passwords,delimiter = ";")
            clear_writer.writerow(["SITE","USERNAME","PASSWORD"]);
            with open(path_plus_filename,mode = 'r') as chrome_exported_passwords:
                for i,row in enumerate(chrome_exported_passwords.readlines()):
                    if(i == 0): # SKIP 'SITE','USERNAME',[...], ROW
                        pass;
                    else:
                        try:
                            items = row.split(',');
                            site_name = items[0];
                            user_name = items[1];
                            password = password_generator.create_password(length_password, charset);
                            clear_writer.writerow([site_name,user_name,password,]);
                        except:
                            items = row.split(';');
                            site_name = items[0];
                            user_name = items[1];
                            password = password_generator.create_password(length_password, charset);
                            clear_writer.writerow([site_name,user_name,password,]);
        # NOW WE CREATE THE NEW FILE CONTAINING ALL THE NEW (encrypted) PASSWORDS
        with open(path + 'list_encrypted_passwords.csv',mode = 'w',newline = "\n") as list_encrypted_passwords:
            encrypted_writer = csv.writer(list_encrypted_passwords,delimiter = ";")
            encrypted_writer.writerow(["SITE","USERNAME","ENCRYPTED PASSWORD"]);
            with open(path + 'list_clear_passwords.csv',mode = 'r') as new_exported_passwords:
                for i,row in enumerate(new_exported_passwords.readlines()):
                    if(i == 0): # SKIP 'SITE','USERNAME',[...], ROW
                        pass;
                    else:
                        items = row.split(';');
                        site_name = items[0];
                        user_name = items[1];
                        password = items[2][:-1]; # password contains also "\n" at the end
                                                  # we don't want to count it
                        caesar_password = caesar_cipher.execute(password);
                        encrypted_writer.writerow([site_name,user_name,caesar_password,]);
    # WE'RE DONE
    print("\n");
    print(">> Please check if there are any errors in the new files");
    print(">> (Like repeated passwords, presence of some old passwords etc.)");
    print(">> [Thank you for your comprehension]\n");
    print(">> Program terminated. Remember: your file(s) are stored in ",path);
