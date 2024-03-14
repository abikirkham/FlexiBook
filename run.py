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

data = schedule.get_all_values()

print(data)

def program_start():
    """
    Displays the programs name and disclaimer 
    """
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
    else:
        print("Invalid option selected!")

def book_class():

def edit_booking():

def cancel_booking():


if __name__ == "__main__":
    main()
