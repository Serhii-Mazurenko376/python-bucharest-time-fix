# Bucharest Time Fix (Python)

A simple Python script to get the current time in **Europe/Bucharest** timezone — useful when your script runs on cloud servers and you need consistent regional time.

## Features

- Uses built-in `zoneinfo` (Python 3.9+)
- Fallback support with `pytz` for older versions
- Shows both UTC and local Bucharest time
- Good base for scheduling, automation, or logs

## Usage

```bash
python bucharest_time.py
```
Expected output:
```
UTC Time:           2025-06-26 08:45:23
Bucharest Time:     2025-06-26 11:45:23 EEST+0300
```
Requirements
	-	Python 3.9+ (zoneinfo included)
	-	or install pytz for compatibility:
 ```
 pip install pytz
```
