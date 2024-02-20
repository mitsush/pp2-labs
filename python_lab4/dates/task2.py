from datetime import datetime, timedelta

print(f'yesterday - {(datetime.today() - timedelta(1)).strftime("%d.%m.%Y")}')
print(f'today - {(datetime.today()).strftime("%d.%m.%y")}')
print(f'tomorrow - {(datetime.today() + timedelta(1)).strftime("%d.%m.%y")}')