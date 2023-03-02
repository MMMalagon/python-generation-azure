from datetime import datetime, timedelta, timezone
from pytz import timezone

import pytz

print(pytz.all_timezones)

print(datetime.now(pytz.timezone("Asia/Tokyo")))
print(datetime.now(pytz.timezone("Europe/Madrid")))
print(datetime.now(pytz.timezone("US/Alaska")))
print(datetime.now(pytz.timezone("UTC")))
