import datetime

print("Hello from master")
day_name = datetime.datetime.now().strftime("%A")
print("Today is:", day_name)

print("Hello from quang-cuong")
today = datetime.date.today()
week_number = today.isocalendar().week  # Lấy số tuần theo ISO
print(f"This week is: {week_number}")

