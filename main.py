#Calculator
from replit import clear
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  '+': add, 
  '-': subtract, 
  '*': multiply, 
  '/': divide,
  }

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for key in operations:
    print(key)
  operation_simbol = input("Pick an operation from the line above: ")
  num2 = float(input("What's the second number?: "))
  calculation_function = operations[operation_simbol]
  first_answer = calculation_function(num1, num2)

  print(f"{num1} {operation_simbol} {num2} = {first_answer}")

  end_calculation = False
  while not end_calculation:
    if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start new calculation.: ") == 'y':
      operation_simbol = input("Pick an operation: ")
      num3 = int(input("What's the next number?: "))
      calculation_function = operations[operation_simbol]
      second_answer = calculation_function(first_answer, num3)

      print(f"{first_answer} {operation_simbol} {num3} = {second_answer}")
      first_answer = second_answer
    else:
      end_calculation = True
      clear()
      calculator()


calculator()