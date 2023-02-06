# Sys module script
import datetime
import os
import sys

print(sys.version)

# os module

print(os.getcwd())

# os.chdir("C:\Users\alexa\Desktop\Sparta Global\Traing courses") # changes current directory

# os.mkdir("path") # makes new directory

# subprocesses module (can be used to create and interact with subprocesses being managed by our python interpreter)


import subprocess
subprocess.run(["python", "hello_world.py"])

#math
import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)
import random

#random
randum = random.randrange(1, 10)
print(randum)

# DateTime
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# json mdodule

import json
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)
print(y)