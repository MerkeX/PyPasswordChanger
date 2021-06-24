
import os,sys,csv,time
from getpass import getuser
import cipher
from tkinter.filedialog import askdirectory, askopenfilename
# WE HAVE TO DRAW A TK ROOT WINDOW BECAUSE IF WE DON'T DO THAT,
# A NEW ONE WILL BE OPENED WHEN ASKING FOR THE FILE
from tkinter import Tk
Tk().withdraw()
from pathlib import Path
from random import randint

class Password:

    # CHARSET ARE SHARED
    global charset_0; global charset_1; global charset_2; global charset_3;
    charset_0 = "abcdefghijklmnopqrstuvwxyz0123456789"
    charset_1 = charset_0 + "@#$%&-.s"
    charset_2 = charset_0 + "ABCDEGHIJKLMNOPQRSTUVWXYZ"
    charset_3 = charset_2 + "@#$%&-."

    def __init__(self,text,charset,length):
        self.text = text
        self.charset = charset
        self.length = length

    def Generate(self,charset,length):
        """
        Return a random string of 'length' containing chars from 'charset'
        """
        l = len(charset) - 1
        passwd = ""
        for i in range(0,length):
            j = randint(0,l)
            passwd = passwd + charset[j]
        return passwd

    def SettingsSelection(self):
        """
        Return charset and length of the password
        """
        # CHARSET SELECTION
        print(":: Charset available: ")

        print(":: 1 - ",charset_0)
        print(":: 2 - ",charset_1)
        print(":: 3 - ",charset_2)
        print(":: 4 - ",charset_3)

        selection = str(input(">> Select charset [1-4]: "))
        if(selection == '1'):
            charset = charset_0
        elif(selection == '2'):
            charset = charset_1
        elif(selection == '3'):
            charset = charset_2
        elif (selection == '4'):
            charset = charset_3
        else:
            print(":: Invalid choice. Default (1) will be used")
            charset = charset_0
        # LENGTH SELECTION
        try:
            length_password = int(input(">> Set password length [6-128]: "))
            if(length_password > 128):
                print(":: Maximum password length reached. Length password will be 128")
                length_password = 128
            if(length_password < 6):
                print(":: Minimum password length not reached. Length password will be 6")
                length_password = 6
            # IF THERE'S ANY ERROR (NEGATIVE NUMBER, LETTERS) JUST PUT A LENGTH OF 16
        except:
            print(":: Incorrect input. Length is set to 16")
            length_password = 16
        self.charset = charset
        self.length = length_password

    def PathSelection(self):
        """
        Let user select the folder in which store the new 
        files with the new passwords. In case no folder is
        selected, or an error occurred with the path (like
        no write permission), file(s) will be stores in Desktop
        (or in the /home folder, for linux use).
        """
        # LET USER SELECT THE FOLDER IN WHICH STORE THE FILE(S)
        # IF THE LOCATION IS INCORRECT OR WE CAN'T ACCESS IT,
        # USE THE 'DESKTOP' FOLDER
        print(">> Select path for password list: ")
        print(":: (Keep in mind that every file previous generated")
        print(":: will be deleted)")
        time.sleep(2)
        try:
            path = askdirectory()
            # SELECTED NO FOLDER, USING DESKTOP AS wORKING DIRECTORY
            if(path == ""):
                print(":: No folder selected. File(s) will be stored in Desktop")
                current_username = getuser()
                if(os.name == "nt"):
                    path =  "C:\\Users\\" + current_username + "\\Desktop"
                elif(os.name == "posix"):
                    path = "/home/" + current_username + "/"
            # SELECTED VALID FOLDER, ADDING SEPARATOR
            if(os.name == "nt"):
                path = path + "/"
            elif(os.name == "posix"):
                path = path + "/"
        # SOME ERRORS OCCURRED, USING DESKTOP AS WORKING DIRECTORY
        except:
            current_username = getuser()
            if(os.name == "nt"):
                path =  "C:\\Users\\" + current_username + "\\Desktop"
            elif(os.name == "posix"):
                path = "/home/" + current_username + "/"
        print(":: File(s) will be created in ",path)
        return path

    def Write(self,mode):
        """
        Write(mode) function:
        - Set 0 if set in single mode (Option (1))
        - Set 1 if set in automated/updater mode (Option (2))
        
        """

        cipher_passwd = cipher.Cipher("")

        path = self.PathSelection()
        pass_text_num = str(input(">> Would you like to write a file with the encrypted passwords?[y/n]: "))
                # CHECK IF THE FILES ARE ALREADY THERE
                # IF SO, WE DELETE THEM
        if(pass_text_num == 'y' or pass_text_num == 'Y'):
            if (os.path.isfile(path + 'list_clear_passwords_new.csv') == 'True'):
                os.remove(path + 'list_clear_passwords_new.csv')
            if (os.path.isfile(path + "list_encrypt_passwords.csv") == 'True'):
                os.remove(path + "list_encrypt_passwords.csv")
            shift = int(input(">> Insert shift [1-25]:  "))
            if(shift > 26):
                print(":: Shift it too big. A shift of ",(shift % 26)," will be used.")
            num_files = 2
        elif(pass_text_num == 'n' or pass_text_num == 'N'):
            if (os.path.isfile(path + "list_clear_passwords_new.csv") == 'True'):
                os.remove(path + "list_clear_passwords_new.csv")
            num_files = 1
        else:
            print(":: Choice not valid. Only the file with the unencrypted passwords will be created.")
            if (os.path.isfile(path + "list_clear_passwords_new.csv") == 'True'):
                os.remove(path + "list_clear_passwords_new.csv")
            num_files = 1
        
        # SINGLE MODE
        if(mode == 0):
            with open(path + 'list_clear_passwords_new.csv',mode = 'w',newline = "\n") as list_clear_passwords,\
            open(path + 'list_encrypt_passwords_new.csv',mode = 'w',newline = "\n") as list_encrypted_passwords:
                clear_writer = csv.writer(list_clear_passwords,delimiter = ";")
                clear_writer.writerow(["GROUP","SITE","USERNAME","CLEAR PASSWORD"])
                if(num_files == 2):
                    encrypted_writer = csv.writer(list_encrypted_passwords,delimiter = ";")
                    encrypted_writer.writerow(["GROUP","SITE","USERNAME","ENCRYPTED PASSWORD"])
                flag = 0; group_name = "Root"
                while(flag == 0):
                    site_name = str(input(">> Insert site: "))
                    # site_name[0] == " " --> USER CAN INSERT ANY NUMBER OF SPACES
                    # 'site_name' IS ALWAYS INVALID; JUST CHECK THE FIRST CHAR
                    while(site_name == "" or site_name[0] == " "):
                        print(":: 'Site' can't be empty. Retry")
                        site_name = str(input(">> Insert site: "))
                    user_name = str(input(">> Insert username: "))
                    # user_name[0] == " " --> SAME AS 'user_name'
                    while(user_name == "" or user_name[0] == " "):
                        print(":: 'username' can't be empty. Retry")
                        user_name = str(input(">> Insert username: "))
                    self.SettingsSelection()
                    print(":: Generating password...")
                    self.text = self.Generate(self.charset,self.length)      
                    clear_writer.writerow([group_name,site_name,user_name,self.text,])
                    if(num_files == 2):
                        caesar_password = cipher_passwd.Caesar(self.text,shift) 
                        encrypted_writer.writerow([group_name,site_name,user_name,caesar_password,])
                    print(":: Completed")
                    ans = str(input(">> Repeat?[Y/n] "))
                    if(ans == 'y' or ans == 'Y'):
                        flag = 0
                    else:
                        flag = 1 # WE'RE DONE
            
        # AUTOMATED MODE
        elif (mode == 1):
            print(">> Select the file containing the old passwords: ")
            try:
                path_plus_filename = askopenfilename()
                while(Path(path_plus_filename).suffix != '.csv'):
                    print(":: File selected is not a csv. Retry...")
                    path_plus_filename = askopenfilename()
                    path = os.path.dirname(path_plus_filename)
                    if(os.name == "nt"):
                        path = path + "\\"
                    elif(os.name == "posix"):
                        path = path + "/"
                        # IF NOTHING IS SELECTED, WE CAN'T ACCESS THE FOLDER OR ANYTHING else
                        # PUT THE FILES ON THE DESKTOP
            except:
                print(":: No file selected. Program will now exit")
                sys.exit(0)
            print(":: New file(s) will be stored in " + path)
            with open(path + 'list_clear_passwords_new.csv',mode = 'w',newline = "\n") as list_clear_passwords,\
            open(path + 'list_encrypt_passwords_new.csv',mode = 'w',newline = "\n") as list_encrypted_passwords:
                clear_writer = csv.writer(list_clear_passwords,delimiter = ";")
                clear_writer.writerow(["GROUP","SITE","USERNAME","CLEAR PASSWORD"])
                if(num_files == 2):
                    encrypted_writer = csv.writer(list_encrypted_passwords,delimiter = ";")
                    encrypted_writer.writerow(["GROUP","SITE","USERNAME","ENCRYPTED PASSWORD"])
                with open(path_plus_filename,mode = 'r') as old_exported_passwords:
                    for i,row in enumerate(old_exported_passwords.readlines()):
                        if(i == 0): # SKIP 'GROUP','SITE','USERNAME',[...], ROW
                            pass
                        else:
                            try:
                                items = row.split(';')
                                group_name = items[0]; site_name = items[1]; user_name = items[2]
                                self.text = self.Generate(self.charset,self.length)
                                clear_writer.writerow([group_name,site_name,user_name,self.text,])
                                if(num_files == 2):
                                    caesar_password = cipher_passwd.Caesar(self.text,shift) 
                                    encrypted_writer.writerow([group_name,site_name,user_name,caesar_password,])
                            except:
                                items = row.split(',')
                                group_name = items[0]; site_name = items[1]; user_name = items[2]
                                self.text = self.Generate(self.charset,self.length)
                                clear_writer.writerow([group_name,site_name,user_name,self.text,])
                                if(num_files == 2):
                                    caesar_password = cipher_passwd.Caesar(self.text,shift)
                                    encrypted_writer.writerow([group_name,site_name,user_name,caesar_password,])
                                    
        print(":: Please check if there are any errors in the new files")
        print(":: (like repeated passwords, presence of some old passwords etc.)")
        print(":: [Thank you for your comprehension].\n")
        print(":: Program terminated. Remember: your file(s) are stored in ", path)


    def Single(self):
        self.Write(0)

    def Update(self):
        self.SettingsSelection();
        self.Write(1)
