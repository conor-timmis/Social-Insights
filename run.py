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
SURVEY_RESULTS_SHEET = GSPREAD_CLIENT.open('social_insights')

def greeting():
    print("Welcome to my Social Media Survey\n" +
          "Please take your time and feel free to answer my questions below: ")

def name():
    print("Please enter your name below, it can be full name or just your first name: ")
    sv_name = input()

    return sv_name

def age(sv_name):
    print(f"Welcome {sv_name}, how old are you?")
    sv_age = input()

    return sv_age

def screen_time(sv_name, sv_age, worksheet):
    print(f"Great! Your name is {sv_name}, and you are {sv_age}.\n"+
    "Please share your average screen time daily in hours, this can also include decimals for specificity: ")
    sv_time = input()
    return sv_time

def sv_yesno(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == "yes" or response == "no":
            return response
        else:
            print('Please enter either "Yes" or "No".')
    
def main():
    greeting()
    sv_name = name()
    sv_age = age(sv_name)
    worksheet = SURVEY_RESULTS_SHEET.sheet1
    sv_time = screen_time(sv_name, sv_age, worksheet)
    worksheet.append_row([sv_name, sv_age, sv_time])


main()