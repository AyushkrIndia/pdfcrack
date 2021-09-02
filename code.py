import pikepdf
from termcolor import colored

file = open("text.txtpip")

for password in file:
    try:
        with pikepdf.open("file.pdf",password.strip()) as pdf:
            print(colored("Password Found: {}".format(password),'green'))
            break
    except:
        print(colored("Trying Password: {}".format(password),'red'))
        continue