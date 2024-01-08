import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime



def record_responses_to_sheet(traits, creative_outlet):
    # Load credentials
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

    # Open the existing spreadsheet
    SHEET = GSPREAD_CLIENT.open('be_creative_quiz_responses')
    choices_worksheet = SHEET.worksheet('choices')

    # Record timestamp and user responses
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row_data = [timestamp] + list(traits.values()) + [creative_outlet]
    choices_worksheet.append_row(row_data)


# written on vs - python practised previously - run see if fits with project 

import time

def personality_quiz():
    print("Welcome to the Personality Quiz!")
    time.sleep(1)
    print("Answer the following questions to discover your ideal creative outlet.\n")

    # Initialize personality trait scores
    traits = {
        'introvert_extrovert': 0,
        'analytical_creative': 0,
        'organized_free_spirited': 0,
        'adventurous_stable': 0
    }

    # Personality questions
    questions = {
        'introvert_extrovert': "1. Do you prefer spending time alone or with a group of people? (Enter 'A' for Alone, 'G' for Group): ",
        'analytical_creative': "2. Are you more analytical or creative? (Enter 'A' for Analytical, 'C' for Creative): ",
        'organized_free_spirited': "3. Do you prefer a structured routine or enjoy spontaneity? (Enter 'S' for Structured, 'F' for Free-spirited): ",
        'adventurous_stable': "4. Are you more adventurous or prefer stability? (Enter 'D' for Adventurous, 'S' for Stable): "
    }

    # Collect user responses
    for trait, question in questions.items():
        answer = input(question).upper()
        if answer == 'A':
            traits[trait] += 1
        elif answer == 'G':
            traits[trait] -= 1

    # Determine creative outlet based on personality traits
    creative_outlet = determine_creative_outlet(traits)

    # Display result and tips
    display_result(creative_outlet)

def determine_creative_outlet(traits):
    if traits['introvert_extrovert'] >= 0 and traits['analytical_creative'] >= 0:
        return 'Writing'
    elif traits['introvert_extrovert'] >= 0 and traits['analytical_creative'] < 0:
        return 'Painting'
    elif traits['introvert_extrovert'] < 0 and traits['analytical_creative'] >= 0:
        return 'Programming'
    else:
        return 'Outdoor Photography'

def display_result(creative_outlet):
    print("\nYour ideal creative outlet is:", creative_outlet)
    
    # Tips and tricks based on creative outlet
    if creative_outlet == 'Writing':
        print("\nTips to get started with writing:")
        print("- Start with short stories or journaling.")
        print("- Find a quiet and comfortable space to write.")
        print("- Set specific goals for your writing sessions.")

    elif creative_outlet == 'Painting':
        print("\nTips to get started with painting:")
        print("- Experiment with different painting techniques and styles.")
        print("- Invest in quality brushes and paints.")
        print("- Attend local art classes or workshops for guidance.")

    elif creative_outlet == 'Programming':
        print("\nTips to get started with programming:")
        print("- Choose a programming language based on your interests.")
        print("- Use online resources and tutorials to learn the basics.")
        print("- Work on small projects to apply your knowledge.")

    elif creative_outlet == 'Outdoor Photography':
        print("\nTips to get started with outdoor photography:")
        print("- Invest in a good quality camera and lens.")
        print("- Explore different outdoor environments for diverse shots.")
        print("- Learn about composition and lighting in photography.")

    # Ask if the user wants to take the quiz again
    restart = input("\nWould you like to take the quiz again? (Enter 'Yes' or 'No'): ").lower()
    if restart == 'yes':
        personality_quiz()
    else:
        print("Thank you for taking the Personality Quiz!")
 record_responses_to_sheet(traits, creative_outlet)

if __name__ == "__main__":
# Run the personality quiz
personality_quiz()
