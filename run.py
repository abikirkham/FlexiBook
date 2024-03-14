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
    typing_print("In this application, you will be able to book "
                 "your favourite yoga class at the date and time "
                 "most suited to you schedule.")
    disclaimer()

    def disclaimer():
        """
        Prints a disclaimer that informs the user about the storae of the input and provoded the possibility to end te application by asking to continue.
        

        Raises:
            ValueError, if the answer to continue wasn't given, is a number, or is not y, yes, n or no
        """
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
    options = ["Book a class", "Edit your booking", "Cancel your booking"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()