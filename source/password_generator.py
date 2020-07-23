
# Simple script to generate a single password
#
# Get length and charset as input, and return a random string

from random import randint

charset_0 = "abcdefghijklmnopqrstuvwxyz0123456789";
charset_1 = charset_0 + "@#$%&";
charset_2 = charset_0 + "ABCDEGHIJKLMNOPQRSTUVWXYZ";
charset_3 = charset_2 + "@#$%&";

def create_password(length,charset):
    l = len(charset) - 1;
    passwd = "";
    for i in range(0,length):
        j = randint(0,l);
        passwd = passwd + charset[j];
    return passwd;
