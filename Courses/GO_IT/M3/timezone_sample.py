from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_time  = datetime( 2026, 6, 15, 12, tzinfo=timezone.utc)

new_york_time = utc_time.astimezone(ZoneInfo("America/New_York"))
print(new_york_time)