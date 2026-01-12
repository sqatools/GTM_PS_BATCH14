from datetime import datetime, timedelta

today_date = datetime.now()
print(today_date) # 2026-01-05 21:49:53.768671
print("date :", today_date.date()) # date : 2026-01-05
print("month :", today_date.month)
print("day :", today_date.day)
print("year :", today_date.year)

# output in string formatting
result = today_date.strftime("%d_%m_%Y_%H_%M_%S")
print("result :", result) # 05_01_2026_21_54_13

# get past date or future.

# get past date.
day_2_prior = today_date - timedelta(days=2)
print(day_2_prior.date())  # 2026-01-03

day_2_ago = today_date + timedelta(days=2)
print(day_2_ago.date()) # 2026-01-07