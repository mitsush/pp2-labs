# Example 1
print("Hello")
print('Hello')

# Example 2
a = "Hello"
print(a)

# Example 3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Example 4
a = "Hello, World!"
print(a[1])

# Example 5
for x in "banana":
    print(x)

# Example 6
a = "Hello, World!"
print(len(a))

# Example 7
b = "Hello, World!"
print(b[2:5])

# Example 8
b = "Hello, World!"
print(b[:5])

# Example 9
b = "Hello, World!"
print(b[2:])

# Example 10
b = "Hello, World!"
print(b[-5:-2])

# Example 11
a = "Hello, World!"
print(a.upper())

# Example 12
a = "Hello, World!"
print(a.lower())

# Example 13
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Example 14
a = "Hello, World!"
print(a.replace("H", "J"))

# Example 15
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Example 16
a = "Hello"
b = "World"
c = a + b
print(c)

# Example 17
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Example 18
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Example 19
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Example 20
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Example 21
txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
