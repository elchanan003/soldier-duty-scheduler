from data import soldiers
from utils import find_soldier_by_id, find_duty_by_name, soldier_has_duty, is_valid_day, is_valid_status


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    soldier = find_soldier_by_id(soldier_id)

    if not soldier:
        raise KeyError ('The id address is not in the system')
    elif soldier_has_duty(soldier, duty_name):
        raise ValueError ('A duty with this name already exists for a soldier')
    elif not is_valid_day(day):
        raise ValueError ('The day entered is invalid')
    else:
        duties = soldier['duties']
        duty = {
            'name'   : duty_name,
            'day'    : day,
            'status' : 'pending'
        }

        duties.append(duty)



def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    soldier = find_soldier_by_id(soldier_id)

    if not soldier:
        raise KeyError('The id address is not in the system')
    if not soldier_has_duty(soldier, duty_name):
        raise KeyError ('No duty was found in this name')
    if not is_valid_status(new_status):
        raise ValueError ('The status entered is incorrect')

    duties = soldier['duties']
    duty = find_duty_by_name(duties, duty_name)

    duty['status'] = new_status


def get_soldier_duties(soldier_id: int) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.

    סוג: גישה לנתונים (Data Access)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת

    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    pass