from datetime import datetime

def format_date(date: datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M:%S")
