from data import soldiers
from utils import find_soldier_by_id, soldier_has_duty, is_valid_id, is_valid_name, get_id, get_name, get_day, get_duty_status
from duty_manager import update_duty_status
from soldier_manager import add_soldier, remove_soldier, get_all_soldiers
from duty_manager import add_duty_to_soldier, get_soldier_duties


def show_menu() -> None:
    menu = """
    ╔══════════════════════════════════════════════╗
    ║        SOLDIER DUTY SCHEDULER SYSTEM         ║
    ╠══════════════════════════════════════════════╣
    ║                                              ║
    ║              Soldier management              ║
    ║                                              ║
    ║    1. Adding a new soldier                   ║
    ║    2. Removing a soldier from the system     ║
    ║    3. Viewing all soldiers                   ║
    ║                                              ║
    ╠══════════════════════════════════════════════╣
    ║                                              ║
    ║              Duties management               ║
    ║                                              ║
    ║    4. Adding a soldier to duty               ║
    ║    5. Duty status update                     ║
    ║    6. Watching a soldier's duties            ║
    ║                                              ║
    ╠══════════════════════════════════════════════╣
    ║                                              ║
    ║    0. Logout                                 ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """

    print(menu)


def get_user_choice() -> str:
    valid = '0123456'
    choice = ''

    while choice not in valid:
        choice = input('Enter your choice: [0-6]')
        if choice not in valid:
            print('Invalid choice, please select a number between 0 and 6')

    return choice


def handle_add_soldier() -> None:
    new_name = get_name()
    new_id = get_id()

    try:
        add_soldier(int(new_id), new_name)
        print('Soldier added successfully!')
    except ValueError as e:
        print(f'Error: {e}')


def handle_remove_soldier() -> None:
    new_id = get_id()

    try:
        remove_soldier(int(new_id))
        print("Soldier removed successfully")
    except KeyError as e:
        print(f'Error: {e}')


def handle_view_soldiers() -> None:
    soldiers = get_all_soldiers()

    for index, soldier in enumerate(soldiers, start=1):
        print(f"{index}. {soldier.get('name')} - ID: {soldier.get('id')} - {soldier.get('duties')}")


def handle_add_duty() -> None:
    soldier_id = get_id()
    day = get_day()
    duty = input('Enter a duty: ')

    try:
        add_duty_to_soldier(soldier_id, duty, day)
        print('Duty added successfully!')
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_update_duty_status() -> None:
    soldier_id = get_id()
    duty = input('Enter a duty: ')
    duty_status = get_duty_status()

    try:
        update_duty_status(soldier_id, duty, duty_status)
        print('Duty status updated successfully!')
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_view_soldier_duties() -> None:
    try:
        soldier_id = get_id()
        duties = get_soldier_duties(soldier_id)
        if not duties:
            print('No duties assigned to this soldier')
        else:
            for index, duty in enumerate(duties, start=1):
                print(f"{index}. {duty.get('name')} - Day: {duty.get('day')} #{duty.get('status')}")

    except KeyError as e:
        print(f'Error: {e}')


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    pass