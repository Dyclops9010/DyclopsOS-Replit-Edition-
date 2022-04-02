import os

print("""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
Type "exit" to exit
""")
while True:
  file_directory = "user/documents/" + input("File name: ")
  if file_directory == "user/documents/exit":
    os.system('python home.py')
  else:
    file = open(file_directory, "w")
    file.write(input("-> "))
    file.close
    file = open(file_directory, "r")
    print("""
You have written the following text to the file:

          
          """)
    print(file.read())