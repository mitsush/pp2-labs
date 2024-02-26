import re

pattern = re.compile("(?=[A-Z])")
print(re.split(pattern, "IchMagLuftballons"))
