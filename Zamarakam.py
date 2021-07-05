import time
import os, sys, subprocess


print("""

░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░
""")

print("""
[1] Continue to setup
[2] Setup is already completed
""")

setup = input("[?]: ")
if setup == "1":
    uname = input(str("Username: "))
    passwd = input(str("Password: "))
    
    with open('.username', 'w') as f:
        f.writelines(uname)
    
    with open('.password', 'w') as f:
        f.writelines(passwd)
    print("Setup is complete! Enjoy Zamarakam OS")
    input("Press Enter to close Window:")

if setup == '2':
    login_passwd  = open(".password")
    login_uname  = open(".username")
    l_p = login_passwd.read()
    l_u = login_uname.read()

while True:
    login = input(str("Password for " + l_u + ": "))
    if login == l_p:
        # if sys.platform == "win32":
            import home

            break
    else:
        print("Password is incorrect")
