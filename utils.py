# אחריות: פונקציות עזר שחוזרות על עצמן
# ============================================================================
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
    """
    בודקת אם לחייל יש תורנות עם שם מסוים.

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        soldier (dict): מילון של חייל
        duty_name (str): שם התורנות לבדיקה

    מחזירה:
        bool: True אם התורנות קיימת לחייל
              False אם לא קיימת

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקה זו משמשת בהוספת תורנות (למנוע כפילויות).
    הפרדה של הלוגיקה למקום אחד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    pass


def is_valid_day(day: str) -> bool:
    """
    בודקת אם יום הוא חוקי (לא שישי או שבת).

    סוג: פונקציית validation (בדיקת תקינות)

    מקבלת:
        day (str): היום לבדיקה

    מחזירה:
        bool: True אם היום חוקי (sunday-thursday)
              False אם לא חוקי או אסור (friday/saturday או ערך לא תקין)

    זורקת: כלום - תמיד מחזירה bool

    למה הפונקציה קיימת:
    בדיקת תקינות של יום משמשת בהוספת תורנות.
    הפרדה של לוגיקת הבדיקה למקום אחד.
    בעתיד אפשר לשנות את הימים החוקיים במקום אחד.
    פונקציות validation מחזירות bool ולא זורקות exceptions.
    """
    pass
