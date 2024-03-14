import gspread
from google.oauth2.service_account import Credentials 

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

data = schedule.get_all_values()

print(data)

def write_to_confirmation_sheet(confirmation_code, day, chosen_time, name):
    CONFIRMATION_SHEET.append_row([confirmation_code, day, chosen_time, name])

def program_start():
    program_logo()
    print("FʟᴇxɪBᴏᴏᴋ")
    typing_print("In this application, you will be able to book "
                 "your favourite yoga class at the date and time "
                 "most suited to you schedule.")
    disclaimer()

    def disclaimer():
        print("DISCLAIMER: ")
        print("The data entered is stored in a Google Worksheet for the duration"
          " of use. Once\nall the data has been completed and a topic has been"
          " selected, you can exit the\nprogram. The data entered will then be"
          " deleted automatically.\nPlease ensure that when you start the"
          " program, you go to the end of it, and the\nfarewell message has"
          " been displayed to guarantee that your data has been \ndeleted"
          " correctly."
          )
   

from simple_term_menu import TerminalMenu

def main():
    options = ["[b] Book a class", "[e] Edit your booking", "[c] Cancel your booking"]
    terminal_menu = TerminalMenu(options, title="Select your action")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if menu_entry_index == '[b]':
        book_class()
    elif menu_entry_index == '[e]':
        edit_booking()
    elif menu_entry_index == '[c]':
        cancel_booking()
    elif menu_entry_index == '[v]':
        view_booking()
    else:
        print("Invalid option selected!")



def book_class():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = ['8:30am', '12:00pm', '13:30pm', '15:00pm', '17:45pm']
    
    day = input("Please chose a day of the week:")

    if day.lower() in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        chosen_time = input("Choose a time: ")
        if chosen_time.lower() in ['8:30am', '12:00pm', '13:30pm', '15:00pm', '17:45pm']:
            name = input("Please enter your name:")
            print(f"Booking confirmed for {day} at {chosen_time} for {name}.")
            confirmation = input("Please confirm this is correct (yes/no): ")
            if confirmation.lower() == 'yes':

                confirmation_code = ''.join(random.choices('0123456789', k=6))
                print(f"Your booking is confirmed. Confirmation code: {confirmation_code}")

write_to_confirmation_sheet(confirmation_code, day, chosen_time, name)

            else:
                print("Booking cancelled. Please start again.")
        else:
            print("Invalid time. Please try again.")
    else:
        print("Invalid day. Please try again.")

book_class()

def edit_booking():

    code = input("Please type you class confirmation code: ")

def cancel_booking():

    code = input("Please type you class confirmation code: ")

def view_booking():

    code = input("Please type you class confirmation code: ")

if __name__ == "__main__":
    main()
