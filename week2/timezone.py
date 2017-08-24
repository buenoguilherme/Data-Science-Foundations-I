from datetime import datetime

import pytz

utc = pytz.utc
ist = pytz.timezone('Asia/Kolkata')

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)