import datetime
from datetime import date

yesterday=date.today()-datetime.timedelta(days=1)
today=date.today()
tommorow=date.today()+datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tommorow)