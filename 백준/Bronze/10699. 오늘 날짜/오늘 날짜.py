from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))  # Korea Standard Time (no DST)
print(datetime.now(KST).strftime("%Y-%m-%d"))