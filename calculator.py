import os
class Calculator:
  def add(self,a,b):return a+b
  def subtract(self,a,b):return a-b
  def multiply(self,a,b):return a*b
  def exponential(self,a,b):return a**b
  def division(self,a,b):
    if b == 0:
      raise ZeroDivisionError("Cannot divide by zero")
    return a/b
  def floor_division(self,a,b):
    if b == 0:
      raise ZeroDivisionError("Cannot dvide by zero")
    return a//b 
  def modulus(self,a,b):return a%b
class UserInterface:
  def __init__(self):
    self.history=[]
    self.calc=Calculator()
    self.name=input("Enter your name: ").capitalize()
  def get_input(self):
    try:
      a=float(input("Enter first value: "))
      b=float(input("Enter second value: "))
      return a,b 
    except ValueError:
      print("Please enter valid number")
      return self.get_input()
  def display_menu(self):
    print(f"====Welcome {self.name}'s Calculator====")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Exponential")
    print("5.Division")
    print("6.Floor division")
    print("7.Modulus")
    print("8.Show history")
    print("9.Export history to file")
    print("10.Exit")
  @staticmethod
  def clear_screen():
      os.system('cls' if os.name == 'nt' else 'clear')
  def run(self):
    while True:
      self.clear_screen()
      self.display_menu()
      choice=input("Enter your choice (1-10): ")
      try:
        if choice == "10":
          print("Thanks for using!Goodbye")
          break
        elif choice == "8":
            print(f"\n===All Saved History===\n")
            if self.history:
              for entry in self.history:
                print(entry)
            else:
              print("No history found")
            input("\nPress Enter to continue...")
            continue
        elif choice == "9":
          if self.history:
            with open("calculator_history.txt","w") as f:
              for entry in self.history:
                f.write(entry+"\n")
            print("History exported successfully to calculator_history.txt")
          else:
            print("No history found to export")
          input("\nPress Enter to continue...")
          continue
      except Exception as e:
        print(f"Error:{e}")
      try:
        a,b=self.get_input()
        if choice == "1":
          result=self.calc.add(a,b)
          history_entry=f"{a}+{b}={result}"
          self.history.append(history_entry)
          print(f"\n====Result====\n{history_entry}\n")
        elif choice == "2":
          result=self.calc.subtract(a,b)
          history_entry=f"{a}-{b}={result}"
          self.history.append(history_entry)
          print(f"\n====Result====\n{history_entry}")
        elif choice == "3":
          result=self.calc.multiply(a,b)
          history_entry=f"{a}*{b}={result}"
          self.history.append(history_entry)
          print(f"\n====Result====\n{history_entry}")
        elif choice == "4":
          result=self.calc.exponential(a,b)
          history_entry=f"{a}**{b}={result}"
          self.history.append(history_entry)
          print(f"\n====Result====\n{history_entry}")
        elif choice == "5":
          result=self.calc.division(a,b)
          history_entry=f"{a}/{b}={result}"
          self.history.append(history_entry)
          print(f"\n====Result====\n{history_entry}")
        elif choice == "6":
          result=self.calc.floor_division(a,b)
          history_entry=f"{a}//{b}={result}"
          self.history.append(history_entry)
          print(f"\n====Result====\n{history_entry}")
        elif choice == "7":
          result=self.calc.modulus(a,b)
          history_entry=f"{a}%{b}={result}"
          self.history.append(history_entry)
          print(f"\n====Result====\n{history_entry}")
        else:
          print("Invalid choice!Please select between 1 to 10")
      except Exception as e:
        print(f"Error:{e}")
      input("Please enter to continue...")
UI=UserInterface()
UI.run()