import datetime
from itertools import cycle

utc_time = datetime.datetime.now(datetime.UTC)
print(utc_time) # UTC time

current_time = datetime.datetime.now()
print(current_time) # current time

print(current_time.isoformat()) # YYYY-MM-DDTHH:MM:SS.ssssss


print(current_time.year)  # Output will be in the format: YYYY
print(current_time.month)  # Output will be in the format: MM
print(current_time.day)  # Output will be in the format: DD
print(current_time.hour)  # Output will be in the format: HH
print(current_time.minute)  # Output will be in the format: MM
print(current_time.second)  # Output will be in the format: SS
print(current_time.microsecond)  # Output will be in the format: ssssss


some_datetime = datetime.datetime(year=2025, month=8, day=25, hour=00, minute=00)
print(some_datetime) # 2025-08-25 00:00:00


current_date = datetime.date.today()
print(current_date) # Output will be in the format: YYYY-MM-DD


current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
print(current_date)


# Получить время, которое было ровно 24 часа назад
day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago) # Вчерашнее время и дата


# Вызвать datetime в читаемом виде
current_datetime = datetime.datetime.now()

print(current_datetime.strftime("%A, %d %B %Y")) # Monday, 25 August 2025

# Преобразовать isoformat в datetime
isoformat = "2025-08-25T00:30:30.384294"
my_datetime = datetime.datetime.fromisoformat(isoformat)
print(type(my_datetime)) # <class 'datetime.datetime'>
print(my_datetime) # 2025-08-25 00:30:30.384294