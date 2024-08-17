#!/usr/bin/env python3

# Created while participating in course: Zaid Security - Learn Ethical Hacking from Scratch with Python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.parse_args()

interface = input("interface >")
new_mac = input()

print("Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])