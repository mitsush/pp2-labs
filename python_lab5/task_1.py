import re

pattern = re.compile("^[a]{1}[b]+$")
print(pattern.search("abb"))
