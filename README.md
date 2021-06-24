# PyPasswordChanger v2.0

PyPasswordChanger is a simple tool to create new/update passwords from different sites.
It can generate new passwords one-by-one, or can generate new ones obtaining 'username' and
'sitenames' from an exported file from your favourite browser.


MODE: <br />
1 - *Simple execution* <br />
    This mode ask for a site name (google, yahoo, outlook etc.), a username (or
    email), and your passwords settings (length, uppercase or special characters)
    for every password you want to store (time consuming if you want to store a
    lot of passwords). This is meant to be used if you have never saved your passwords
    in a browser or in a password manager.  <br />

2 - *Password updater* <br />
    If you store your passwords in your browser (maybe synced in your Google, Firefox 
    or Edge account), or you use a password manager (like Bitwarden, KeePass, 1Passwords etc.),
    you can export them (in a .csv format) and use this file to obtain the list of your
    site and usernames (the passwords will be ignored).
    You set the passwords settings (length and charset) and you are good to go.
    You have a fresh new file with new passwords to import in your browser or
    password manager. NOTE: before that, you must change them through the site, of course.
    <br />

This tools also offer the option to "encrypt" your password with a simple 'caesar cipher', 
that allows you to print your passwords in a paper or storing in your pc without worrying that 
someone could gain access to all of your sites. (I know there are more useful way to actually 
encrypt your passwords, but if you are going to print them for keeping a offline/backup copy 
without needing a computer, I doubt you can decrypt making calculation in mind. With 'Caesar', 
it's easier to go back to the original password).
In the 'example' folder, there a example .csv file that you can use for testing.

**Usage**

*Windows*

- Download the portable version (v2.0) from [here](https://github.com/MerkeX/PyPasswordChanger/releases/download/2.0/PyPassChanger_Portable-win.zip);<br />
- (it has been created with pyinstaller) <br />
  or<br />
- Download python3 from python.org and install it; <br />
- Download or clone the source folder; <br />
- Run 'python3.exe main.py' from a powershell window. <br />

*Linux*
- Download the portable version (v2.0) from [here](https://github.com/MerkeX/PyPasswordChanger/releases/download/2.0/PyPassChanger_Portable-linux.tar);<br />
  or<br />
- Download or clone the source folder; <br />
- Simply run 'python main.py' on a terminal.

**Disclaimer**
This tool is made by an amateur. I'm sure that there are some bugs, or there more efficient ways to actually do it.

