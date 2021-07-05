import subprocess
import platform
import socket
import time
import os
import sys

path = '/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
login_uname  = open(".username")
l_u = login_uname.read()
print("Welcome to Zamarakam Terminal [V 1.0]")

while True:
    code = input(l_u + ' $ ')
    if code == 'ping':
        host = input("Enter Website to ping: ")
        number = input('Enter Times to ping: ')
        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'info':
        print("local IPS: " + host_ip)
        print("Host name: " + host_name)
        print("User name: " + l_u)
    if code == 'date':
        print("The date is: " + time.strftime("%y/%m/%d"))
    if code == 'ls':
        dir_list = os.listdir(path)
        print("Files and Directories in '", path, "' :")
        print(dir_list)
    if code == 'ls -a':
        file = input("Enter file path to Read: ")
        dir_list2 = os.listdir(file)
        print("Files and Directories in '", file, "' :")
        print(dir_list2)
    if code == 'exit':
        exec(open("home.py").read())
    if code == 'shutdown':
        sys.exit("Closing Zamarakam")
