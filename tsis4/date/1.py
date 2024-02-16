from datetime import datetime, timedelta
now = datetime.now()
five = now - timedelta(days = 5)
print(now.strftime("%Y - %m - %d"))
print(five.strftime("%Y - %m - %d"))