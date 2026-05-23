from data import soldiers
from utils import is_valid_name, find_soldier_by_id

def add_soldier(soldier_id: int, name: str) -> None:
    if not is_valid_name(name):
        raise ValueError ("The name entered is invalid")

    if find_soldier_by_id(soldier_id):
        raise ValueError ('The ID address already exists in the system')

    soldier = {
        'id'    : soldier_id,
        'name'  : name,
        'duties': []
    }

    soldiers.append(soldier)


def remove_soldier(soldier_id: int) -> None:
    soldier = find_soldier_by_id(soldier_id)

    if not soldier:
        raise KeyError ("The id address is not in the system")
    else:
        soldiers.remove(soldier)


def get_all_soldiers() -> list:
    """
    מחזירה את רשימת כל החיילים במערכת.

    סוג: גישה לנתונים (Data Access)

    מקבלת: כלום

    מחזירה:
        list: רשימה של מילונים, כל מילון מייצג חייל
              רשימה ריקה אם אין חיילים

    זורקת: כלום - תמיד מחזירה רשימה (ריקה או מלאה)

    למה הפונקציה קיימת:
    גישה לנתונים בצורה מבוקרת.
    מאפשר לקבל את הנתונים מבלי לגשת ישירות למשתנה הגלובלי.
    """
    pass