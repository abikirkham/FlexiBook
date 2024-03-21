import gspread
import random
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
import colorama
from colorama import Fore, Back, Style


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('FlexiBook')

CONFIRMATION_SHEET = SHEET.worksheet('confirmation')


def write_to_confirmation_sheet(confirmation_code, day, chosen_time, name):
    CONFIRMATION_SHEET.append_row([confirmation_code, day, chosen_time, name])


def book_class():
    """ One line doc string """
    print("""
    Welcome to the class booking stage, please follow the instructions below:
    """)
    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    times = ['8:30am', '12:00pm', '13:30pm', '15:00pm', '17:45pm']

    print(f"""
            {Fore.BLUE}
    Our open days are:
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday
        {Style.RESET_ALL}
    """)
    day = input("Please chose a day of the week you want to book:\n")

    if day.lower() in [
                    'monday',
                    'tuesday',
                    'wednesday',
                    'thursday'
                    'friday',
                    'saturday',
                    'sunday']:
        print(F"""{Fore.BLUE}
        The available times are:
        8:30am, 12:00pm, 13:30pm, 15:00pm, 17:45pm
        {Style.RESET_ALL}
        """)
        chosen_time = input("Choose a time:\n")
        if chosen_time.lower() in [
                                '8:30am',
                                '12:00pm',
                                '13:30pm',
                                '15:00pm',
                                '17:45pm']:
            name = input("Please enter your name:\n")
            print(f"""
            {Fore.YELLOW}
            Booking confirmed for {day} at {chosen_time} for {name}.
            """)
            confirmation = input(f"""
            {Fore.YELLOW}
            Please confirm this is correct (yes/no):\n
            {Style.RESET_ALL}
            """)
            if confirmation.lower() == 'yes':
                confirmation_code = ''.join(random.choices('0123456789', k=6))
                print(f"""
                {Fore.GREEN}
                YAY, booking confirmed. Confirmation code: {confirmation_code}
                {Style.RESET_ALL}
                """)
                write_to_confirmation_sheet(confirmation_code,
                                            day, chosen_time, name)
            else:
                print("Booking cancelled. Please start again.")
        else:
            print(Fore.RED + "Invalid time. Please try again.")
    else:
        print(Fore.RED + "Invalid day. Please try again.")
    input("Press Enter to return to the main menu.")
    main()


def clear_screen():
    print("\033c", end="")


def edit_booking():
    confirmation_code = input(Fore.BLUE + """
    Please type your class confirmation code:\n
    """)
    all_confirmation_codes = CONFIRMATION_SHEET.col_values(1)[1:]
    all_rows = CONFIRMATION_SHEET.get_all_values()[1:]

    if confirmation_code in all_confirmation_codes:
        index = all_confirmation_codes.index(confirmation_code)
        row_to_edit = all_rows[index]

        print(f"""{Fore.GREEN}
        Booking found. What would you like to edit?\n
        {Style.RESET_ALL}""")
        print(Fore.BLUE + "1. Change date\n2. Change time\n")
        choice = input("Enter your choice (1/2):\n")

        new_time = None  # Initialize new_time variable

        if choice == '1':
            new_day = input(Fore.GREEN + "Enter new day:\n")
            row_to_edit[1] = new_day
        elif choice == '2':
            new_time = input(Fore.GREEN + "Enter new time:\n")
            row_to_edit[2] = new_time
        else:
            print(Fore.RED + "Invalid choice. Please enter either 1 or 2.")
            edit_booking()

        print("Changes made. Confirm?\n")
        confirmation = input(f"""{Fore.YELLOW}
        Please confirm this is correct (yes/no):\n
        {Style.RESET_ALL}""")
        if confirmation.lower() == 'yes':
            # Update the Google Sheet with the new values
            if new_time is not None:  # Check if new_time is assigned
                CONFIRMATION_SHEET.update('C' + str(index + 2), [[new_time]])
            CONFIRMATION_SHEET.update('B' + str(index + 2), [[row_to_edit[1]]])
            print(Fore.GREEN + "Booking details updated.")
        else:
            print("Changes discarded.")

    else:
        print("Invalid confirmation code. Please try again.")

    input("Press Enter to return to the main menu.\n")
    main()


def clear_screen():
    print("\033c", end="")


def cancel_booking():
    confirmation_code = input("Please type your confirmation code:\n")
    all_confirmation_codes = CONFIRMATION_SHEET.col_values(1)[1:]
    all_rows = CONFIRMATION_SHEET.get_all_values()[1:]

    if confirmation_code in all_confirmation_codes:
        index = all_confirmation_codes.index(confirmation_code)
        row_to_delete = all_rows[index]

        print(f"""
        {Fore.BLUE}
        Booking found. Are you sure you want to cancel?
        {Style.RESET_ALL}""")
        choice = input(f"""{Fore.YELLOW}
        Enter 'yes' to confirm cancellation, or 'no' to keep the booking:\n
        {Style.RESET_ALL}""")
        if choice.lower() == 'yes':
            CONFIRMATION_SHEET.delete_row(index + 2)
            print("Booking canceled.")
        elif choice.lower() == 'no':
            print(Fore.RED + "You remain on our class booking system.")
        else:
            print(Fore.RED + """
            Invalid choice. Please enter either 'yes' or 'no'.
            """)
    else:
        print(Fore.RED + "Invalid confirmation code. Please try again.")
    input("Press Enter to return to the main menu.\n")
    main()


def clear_screen():
    print("\033c", end="")


def welcome_message():
    """ Welcome mesage function """
    print(Fore.MAGENTA + """
█▄─▄▄─█▄─▄███▄─▄▄─█▄─▀─▄█▄─▄█▄─▄─▀█─▄▄─█─▄▄─█▄─█─▄█
██─▄████─██▀██─▄█▀██▀─▀███─███─▄─▀█─██─█─██─██─▄▀██
▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀
""")
    print("In this application, you will be able to book your favourite "
          "yoga class at the \ndate and time most suited to you schedule.")


def main_menu():

    options = ["[b] Book a class",
               "[e] Edit your booking",
               "[c] Cancel your booking"]
    terminal_menu = TerminalMenu(options, title= Fore.GREEN + """
    Select your action""" + Style.RESET_ALL)
    menu_entry_index = terminal_menu.show()
    print(f"""

{Fore.MAGENTA} You have selected {options[menu_entry_index]}! {Style.RESET_ALL}
    """)
    print(options[menu_entry_index])

    if menu_entry_index == 0:
        book_class()
    elif menu_entry_index == 1:
        edit_booking()
    elif menu_entry_index == 2:
        cancel_booking()
    else:
        print(Fore.RED + "Invalid option selected!")
    input("Press Enter to return to the main menu.")
    main()


def main():
    welcome_message()
    main_menu()


if __name__ == "__main__":
    main()
