import datetime
from datetime import date

five_days_ago=date.today()-datetime.timedelta(days=5)

print(five_days_ago)
