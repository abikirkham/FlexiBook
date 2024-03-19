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

schedule = SHEET.worksheet('schedule')
CONFIRMATION_SHEET = SHEET.worksheet('confirmation')


def write_to_confirmation_sheet(confirmation_code, day, chosen_time, name):
    CONFIRMATION_SHEET.append_row([confirmation_code, day, chosen_time, name])


def book_class():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = ['8:30am', '12:00pm', '13:30pm', '15:00pm', '17:45pm']

    day = input("Please chose a day of the week:\n")

    if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        chosen_time = input("Choose a time:\n")
        if chosen_time.lower() in ['8:30am', '12:00pm', '13:30pm', '15:00pm', '17:45pm']:
            name = input("Please enter your name:\n")
            print(f"Booking confirmed for {day} at {chosen_time} for {name}.")
            confirmation = input("Please confirm this is correct (yes/no):\n")
            if confirmation.lower() == 'yes':
                confirmation_code = ''.join(random.choices('0123456789', k=6))
                print(f"Your booking is confirmed. Confirmation code: {confirmation_code}")
                write_to_confirmation_sheet(confirmation_code, day, chosen_time, name)
            else:
                print("Booking cancelled. Please start again.")
        else:
            print(Fore.RED + "Invalid time. Please try again.")
    else:
        print(Fore.RED + "Invalid day. Please try again.")
    input("Press Enter to return to the main menu.")


def edit_booking():
    confirmation_code = input("Please type your class confirmation code:\n")
    if confirmation_code in CONFIRMATION_SHEET:
        print("Booking found. What would you like to edit?")
        print("1. Change date")
        print("2. Change time")
        choice = input("Enter your choice (1/2):\n")
        if choice == '1':
            book_class()
        elif choice == '2':
            book_class()
        else:
            print(Fore.RED + "Invalid choice. Please enter either 1 or 2.")
            edit_booking()
    else:
        print("Invalid confirmation code. Please try again.")
    input("Press Enter to return to the main menu.\n")


def cancel_booking():
    confirmation_code = input("Please type your class confirmation code:\n")
    if confirmation_code in CONFIRMATION_SHEET:
        print("Booking found. Are you sure you want to cancel?")
        choice = input("Enter 'yes' to confirm cancellation, or 'no' to keep the booking:\n")
        if choice.lower() == 'yes':
            print("Booking cancelled.")
        elif choice.lower() == 'no':
            print(Fore.RED + "You remain on our class booking system.")
        else:
            print(Fore.RED + "Invalid choice. Please enter either 'yes' or 'no'.")
    else:
        print(Fore.RED + "Invalid confirmation code. Please try again.")
    input("Press Enter to return to the main menu.\n")


def main():
    print(Fore.GREEN + "FʟᴇxɪBᴏᴏᴋ")
    print("In this application, you will be able to book your favourite "
          "yoga class at the date and time most suited to you schedule.")
    print("DISCLAIMER: ")
    print("The data entered is stored in a Google Worksheet for the duration"
          " of use. Once\nall the data has been completed and a topic has been"
          " selected, you can exit the\nprogram. The data entered will then be"
          " deleted automatically.\nPlease ensure that when you start the"
          " program, you go to the end of it, and the\nfarewell message has"
          " been displayed to guarantee that your data has been \ndeleted"
          " correctly."
          )

    options = ["[b] Book a class", "[e] Edit your booking", "[c] Cancel your booking"]
    terminal_menu = TerminalMenu(options, title="Select your action")
    menu_entry_index = terminal_menu.show()
    print(Fore.MAGENTA + f"You have selected {options[menu_entry_index]}!")

    if menu_entry_index == '[b]':
        book_class()
    elif menu_entry_index == '[e]':
        edit_booking()
    elif menu_entry_index == '[c]':
        cancel_booking()
    else:
        print(Fore.RED + "Invalid option selected!")


if __name__ == "__main__":
    main()
