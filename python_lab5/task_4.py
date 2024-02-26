import re

pattern = re.compile("[A-Z]{1}[a-z]+")
print(pattern.search("Miras"))
