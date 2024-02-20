from datetime import datetime

current_time = datetime.now()
print(current_time.strftime("%d.%m.%Y %H:%M:%S"))

# current_time = datetime.now()
# current_time = current_time.replace(microsecond=0)
# print(current_time)