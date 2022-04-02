import os

print("""
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
1. Text Editor
2. Text Reader
3. Text Appender (add more to file)
4. Leave
      """)

choice = input("-> ")

if choice == "1":
  os.system('python apps/text_writer.py')
if choice == "2":
  os.system('python apps/text_reader.py')
if choice == "3":
  os.system('python apps/text_appender.py')
if choice == "4":
  os.system('python home.py')