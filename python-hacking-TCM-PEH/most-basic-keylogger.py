##This does not currently do anything interesting other than showing a concept

from getkey import *
from datetime import datetime
now = datetime.now()

while True:
  key = getkey()
  print(key)