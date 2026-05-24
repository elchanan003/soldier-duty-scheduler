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

def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    duties = soldier.get("duties")
    return find_duty_by_name(duties, duty_name) is not None

def is_valid_status(status: str) -> bool:
    valid_status = ["pending", "completed", "missed"]
    return status in valid_status

def is_valid_name(name: str) -> bool:
    return len(name.strip()) > 0

def is_valid_day(day: str) -> bool:
    valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
    return day.lower() in valid_days

def is_valid_id(id_num: str) -> bool:
    id_num = id_num

    if len(id_num) != 9:
        return False
    if not id_num.isdigit():
        return False

    return True

def get_id() -> int:
    new_id = ''
    while not is_valid_id(new_id):
        new_id = input('Enter a ID number: ')

    return int(new_id)

def get_name() -> str:
    new_name = ''
    while not is_valid_name(new_name):
        new_name =  input('Enter a name: ')

    return new_name

def get_day() -> str:
    day = ''

    while not is_valid_day(day):
        day =  input('Enter a day: ')

    return day

def get_duty_status():
    status = ''

    while not is_valid_status(status):
        status =  input('Enter a status: ')

    return status
