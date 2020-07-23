# PyPasswordChanger v1.0

PyPasswordChanger is a simple tool to create new/update passwords from different sites.
It can generate new passwords one-by-one, or can generate new ones obtaining 'username' and
'sitenames' from an exported file from your favourite browser.
If can also use a 'caesar cipher', that allows you to print your passwords in a paper
without worrying that someone could gain access to all of your sites. It offers the
possibility to store your clear passwords and ciphered passwords in the same file
or in two distinct files.
In the 'example' folder, there a example .csv file that you can use for testing

MODE: <br />
1 - *Simple execution* <br />
    This mode ask for a site name (google, yahoo, outlook etc.), a username (or
    email), and your passwords settings (length, uppercase or special characters)
    for every password you want to store (time consuming if you want to store a
    lot of passwords); <br />
2 - *Automated process* <br />
    This mode requires that you have a browser-exported file with your saved password
    (.csv format)[tested with Google Chrome]; from
    this file, it obtains site name and username; then, you insert your passwords
    settings (length, [...]), and you'll have a list of your new passwords
    (clear ones and encrypted one can be stored in the same file or in different
    files). <br />
3 - *Password updater* <br />
    This mode is useful if you already have used this tool before, and you want
    to update your passwords, without needing to export a new file from your browser.
    Same as before, you just have to insert your passwords settings, and you are
    good to go. <br />

**Usage**

*Windows*

- Download the portable version from [here](https://github.com/MerkeX/PyPasswordChanger/releases/download/1.0/PyPassChanger_Portable-win.zip);<br />
- (it has been created with pyinstaller) <br />
  or<br />
- Download python3 from python.org and install it; <br />
- Download or clone the source folder; <br />
- Run 'python3 main.py' from a powershell window. <br />

*Linux*
- Download the portable version from [here](https://github.com/MerkeX/PyPasswordChanger/releases/download/1.0/PyPassChanger_Portable-linux.tar);<br />
  or<br />
- Download or clone the source folder; <br />
- Simply run 'python main.py' on a terminal.
