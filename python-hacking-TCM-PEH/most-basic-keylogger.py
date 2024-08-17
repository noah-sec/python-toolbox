# Created while participating in course: TCM Security - Practical Ethical Hacking (The Complete Course)
##This does not currently do anything interesting other than showing a concept

from getkey import *
from datetime import datetime
now = datetime.now()

while True:
  key = getkey()
  print(key)