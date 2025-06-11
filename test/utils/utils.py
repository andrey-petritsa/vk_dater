import json
from datetime import datetime


def save(data, tag):
    #path = f'dbg_ignore/dbg-{get_current_datetime_string()}-{tag}.json'
    with open(fr'dbg_ignore/dbg-{get_current_datetime_string()}-{tag}.json', "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4, sort_keys=False, default=str)

def get_current_datetime_string():
    now = datetime.now()
    return f"{now.day:02d}-{now.hour:02d}-{now.minute:02d}-{now.second:02d}"

