from datetime import datetime, timezone

def iso_time():
    now_utc = datetime.now(timezone.utc)
    iso_utc = now_utc.isoformat()
    return iso_utc

