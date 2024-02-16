from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days = 1)
difference = today - yesterday
in_second = difference.total_seconds()
print(in_second)