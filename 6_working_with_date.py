from datetime import datetime

# Get the current date and time
current = datetime.now()
print(current)

formatted = current.strftime("%d/%m/%Y %H:%M:%S")
print(formatted)
# more format date option: https://www.w3schools.com/python/python_datetime.asp

# Create a date
date = datetime(2021, 2, 14)
print(date)

# Create a date with time
date_time = datetime(2022, 2, 14, 12, 30, 45)
print(date_time)

# calculate date with date
date_apart = date_time - date
print(date_apart)
print(date_apart.days)
print(date_apart.total_seconds()/ 60)
