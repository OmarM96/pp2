import datetime
from datetime import time
from datetime import datetime
datetime_string="11/02/2024 15:35:02"
today=datetime.now()
time_object=datetime.strptime(datetime_string, "%m/%t/%y %H:%M:%S")

print(time_object)