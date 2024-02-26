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
SHEET = GSPREAD_CLIENT.open('social_insights')

def greeting():
    print("Welcome to my Social Media Survey\n" +
          "Please take your time and feel free to answer my questions below: ")

def name():
    print("Please enter your name below: ")
    first_name = input()
    print(f"Welcome {first_name}, how old are you?")

def main():
    greeting()
    name()

main()