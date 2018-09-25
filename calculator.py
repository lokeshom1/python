def help_screen():
     print("Add : Adds 2 numbers")
     print("Subtract : Substracr 2 numbers")
     print("print: Display the result of the latest operation")
     print("Help : Display this help screen")
     print("Quit: EXists the program")

def menu():
     return input("==A)dd S)ubstracrt P)rint H)elp Q)uit")

def main():
     result=0
     done=False
     while not done:
          choice = menu()

          if choice == "A" or choice =="a":
               arg1=float(input("Enter the arg1:"))
               arg2=float(input("Enter the arg2:"))
               result=arg1+arg2
               print(result)
          elif choice == "S" or choice =="s":
               arg1=float(input("Enter the arg1:"))
               arg2=float(input("Enter the arg2:"))
               result=arg1-arg2
               print(result)
          elif choice =="P" or choice =="p":
               print(result)
          elif choice =="H" or choice =="h":
               help_screen()
          elif choice == "Q" or choice =="q":
               done=True
main()
               
