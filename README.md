# Scripting 

- scripting is used in programing to automate processes for websites and web applications. it is short pieces of code that allows us to do things we would otherwise have to do manually.
- -unlike programs, scripts are one file and do not need to be compiled
- API' tend to use scripts 
- Websites, applications, and programs need scripting in order to function efficiently. Scripting is used in program testing and also automates different processes within a program.
- scripts use less or no abstraction and are not as flexible as programs. but they are much easier to read and write. 
- scripts are almost always written in high level languages (easy to read) Python, Bash, Ruby, Node.js
### Why python for scripting?
- Python is used for scripting as it is simple and its syntax is easy to learn also it emphasizes readability and has a low cost of maintenance.
- DevOps engineers use scripting to automate tasks within an operating system and enhance web pages within browser software. 
- Many libraries 
- Really large community
- languages interoperability (can talk to other languages, OS's and software)
- automation of mundane tasks. 

### 7 core modules 
- Sys
```python
import sys 
print(sys.version)
```
- Os
```python
import os

print(os.getcwd())
```
- Subprocesses
```python
import subprocess
subprocess.run(["python", "hello_world.py"])
```

- Math
```python
import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)
```
- Random
```python
randum = random.randrange(1, 10)
print(randum)
```
```python
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)
```
- Json
