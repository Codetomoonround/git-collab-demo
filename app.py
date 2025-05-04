import datetime

print("Hello from master")
day_name = datetime.datetime.now().strftime("%A")
print("Today is:", day_name)

print("Hello from quang-cuong")
today = datetime.date.today()
week_number = today.isocalendar().week  # Lấy số tuần theo ISO
print(f"This week is: {week_number}")

print("Hello from dinh-ha")

# Danh sách 12 con giáp
zodiacs = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Lấy năm hiện tại
year = datetime.datetime.now().year

# Tính chỉ số con giáp
index = (year - 4) % 12  # Vì năm 4 (Giáp Tý) là khởi đầu

print(f"Năm nay là năm con {zodiacs[index]} ({year})")
