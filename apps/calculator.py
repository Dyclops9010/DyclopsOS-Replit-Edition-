import os

print("""
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      












































      
██████╗░██╗░░░██╗██╗░░░░░██╗░░░██╗░█████╗░████████╗░█████╗░██████╗░
██╔══██╗╚██╗░██╔╝██║░░░░░██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║░╚████╔╝░██║░░░░░██║░░░██║███████║░░░██║░░░██║░░██║██████╔╝
██║░░██║░░╚██╔╝░░██║░░░░░██║░░░██║██╔══██║░░░██║░░░██║░░██║██╔══██╗
██████╔╝░░░██║░░░███████╗╚██████╔╝██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░░░░╚═╝░░░╚══════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
      """)



while True:
  print("""
Choice 1: Addition
Choice 2: Subtraction
Choice 3: Divide
Choice 4: Multiply
Choice 5: Exit
""")
  choice = input("Chose: ")
  if choice == "1":
    number1 = float(input("Number 1: "))
    number2 = float(input("Number 2: "))
    print(number1 + number2)
  if choice == "2":
    number1 = float(input("Number 1: "))
    number2 = float(input("Number 2: "))
    print(number1 - number2)
  if choice == "3":
    number1 = float(input("Number 1: "))
    number2 = float(input("Number 2: "))
    print(number1 / number2)
  if choice == "4":
    number1 = float(input("Number 1: "))
    number2 = float(input("Number 2: "))
    print(number1 * number2)
  if choice == "5":
    break
  break
os.system('python home.py')