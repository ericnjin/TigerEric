
from datetime import datetime

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss

Now save and exit the file and run it by:
$ python dateParser.py

Time.sleep

In Python you can use time.sleep() to suspend execution for the given number of
seconds.

The seconds are being given between the parenthesis.

# How to sleep for 5 seconds in python:

import time

time.sleep(5)

# How to sleep for 0.5 seconds in python:

import time

time.sleep(0.5
