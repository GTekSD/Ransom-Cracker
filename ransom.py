print("_________________________________________________________")
print("                        GTekSD                           ")
print(" █▀█ ▄▀█ █▄░█ █▀ █▀█ █▀▄▀█   █▀▀ █▀█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█ ")
print(" █▀▄ █▀█ █░▀█ ▄█ █▄█ █░▀░█   █▄▄ █▀▄ █▀█ █▄▄ █░█ ██▄ █▀▄ ")
print("             Decrypt Encrypted Files v1.3                ")
print("_________________________________________________________")
print("                                                         ")

import zipfile

def crack_password(password_list, obj):

    # tracking line no. at which password is found
    idx = 0
 
    # open file in read byte mode only as "rockyou.txt"
    # file contains some special characters and hence
    # UnicodeDecodeError will be generated
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print(" ")
                    print("[+] Performing password attack on",zip_file)
                    print(" ")
                    print("[!] Valid Combinations Found: line =", idx)
                    print(" |  Password:", word.decode())
                    return True
                except:
                    continue
    return False
 
 
# Enter encrepted zip file name here.
zip_file = input("Enter encrypted .zip file name:")

# Replace password file with any other if password not found.
password_list = input("(Passwds list:")

# ZipFile object initialised
obj = zipfile.ZipFile(zip_file)
 
# count of number of words present in file
cnt = len(list(open(password_list, "rb")))
 
if crack_password(password_list, obj) == False:
    print(" ")
    print("[i] No Valid Passwords Found.")
    print(" |  There are total", cnt, "number of passwords combinations are not valid.")
    print("[+] _______________________________________________________________________")
    print(" |  Try different wordlist from SecLists/Passwords !")
 
