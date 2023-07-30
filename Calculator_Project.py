# importing logo from another module
import art_for_calculator
import os

#defining function for the calculation
def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

# creating a dictionary for every key to the value of operation
operation =  {
  "+": add,
  "*": multiply,
  "-": subtract,
  "/": divide
}

# Defining the function for calculations
def calculator():
  print(art_for_calculator.logo)
  
  num1 = float(input("What's the first number?: "))
  for symbol in operation:
    print(symbol)

  should_continue = True

# Repeatiting the process until you end the calculations
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Enter the next digit: "))
    operation_function = operation[operation_symbol]
    answer = operation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
      
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls||clear')
      calculator()

# Calling the function for the first time
calculator()