import os

f = open("user/info.data", "r")

if f.read() == "1":
  os.system('python login.py')
else:
  os.system('python setup.py')