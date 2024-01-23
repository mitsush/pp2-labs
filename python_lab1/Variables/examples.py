# Example 1
x = 5
y = "John"
print(x)
print(y)

# Example 2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Example 3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Example 4
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Example 5
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Example 6
x = 5
y = "John"
print(type(x))
print(type(y))

# Example 7
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Example 8
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Example 9
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Exampl 10
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Example 11
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

