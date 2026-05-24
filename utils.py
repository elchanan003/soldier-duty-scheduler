from data import soldiers


def find_soldier_by_id(soldier_id: int) -> dict | None:
    for soldier in soldiers:
        if soldier.get("id") == soldier_id:
            return soldier
    return None

def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    for duty in duties:
        if duty.get("name") == duty_name:
            return duty
    return None

def is_valid_status(status: str) -> bool:
    valid_status = ["pending", "completed", "missed"]
    return status in valid_status

def is_valid_name(name: str) -> bool:
    return len(name.strip()) > 0

def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    duties = soldier.get("duties")
    return find_duty_by_name(duties, duty_name) is not None

def is_valid_day(day: str) -> bool:
    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    return day in valid_days

def is_valid_id(id_num: int) -> bool:
    id_num = str(id_num)

    if len(id_num) != 9:
        return False
    if not id_num.isdigit():
        return False

    return True





