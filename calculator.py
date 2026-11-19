def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def square(a):
  return a*a

def divide(a, b):
  if b == 0:
    return  "Error: division by zero"
  return a / b

def power(a, b):
  return a ** b

def mod(a, b):
  return a % b

def cube(a):
  return a*a*a

def absolute(a):
  if a < 0:
    return -a
  return a


if __name__ == "__main__":
  print("2 + 3 =", add(2, 3))
  print("5 - 2 =", subtract(5, 2))
  print("2 * 3 =", multiply(2, 3))
  print("2^2 =", square(2))
  print("3 / 0 =", divide(3, 0))
  print("2 ** 3 =", power(2,3))
  print("10 % 3 =", mod(10,3))
  print("3 cubed =", cube(3))
  print("absolute(-5) =", absolute(-5))
