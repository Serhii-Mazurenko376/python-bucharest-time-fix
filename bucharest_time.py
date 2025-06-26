from datetime import datetime

try:
    from zoneinfo import ZoneInfo
    def get_bucharest_time():
        return datetime.now(ZoneInfo("Europe/Bucharest"))
except ImportError:
    import pytz
    def get_bucharest_time():
        tz = pytz.timezone("Europe/Bucharest")
        return datetime.now(tz)

def main():
    utc_now = datetime.utcnow()
    local_bucharest = get_bucharest_time()

    print("UTC Time:           ", utc_now.strftime('%Y-%m-%d %H:%M:%S'))
    print("Bucharest Time:     ", local_bucharest.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

if __name__ == "__main__":
    main()
