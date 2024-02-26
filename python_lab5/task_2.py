import re

pattern = re.compile("^[a]{1}[b]{2,3}$")
print(pattern.search("abbb"))
