from datetime import datetime, timedelta
today_date = datetime.now()
print(today_date)
print("date :", today_date.date())
print("month :", today_date.month)
print("day :", today_date.day)
print("year :", today_date.year)

# output in string formatting
result = today_date.strftime("%d_%m_%Y_%H_%M_%S")
print("result :", result)
# get past date or future.
# get past date.
day_2_prior = today_date - timedelta(days=2)
print(day_2_prior.date())
day_2_ago = today_date + timedelta(days=2)
print(day_2_ago.date())


#get specific past date
specific_past_date = today_date - timedelta(days=10, hours=5, minutes=30)
print(specific_past_date)
print(specific_past_date.date())
# get future date
future_date = today_date + timedelta(days=5)
print(future_date.date())
future_date_time = today_date + timedelta(days=5, hours=3, minutes=30)
print(future_date_time)
print(future_date_time.date())

# get difference between two dates
date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 1, 1)
difference = date2 - date1
print("Difference between", date2.date(), "and", date1.date(), "is", difference.days, "days.")
# get current time
current_time = today_date.time()
print("Current Time:", current_time)
# add hours and minutes to current time
new_time = (datetime.combine(datetime.today(), current_time) + timedelta(hours=2, minutes=15)).time()
print("New Time after adding 2 hours and 15 minutes:", new_time)
