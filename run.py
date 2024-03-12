import gspread
from google.oauth2.service_account import Credentials
import os


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SURVEY_RESULTS_SHEET = GSPREAD_CLIENT.open('social_insights')
NAME = None
AGE = 0


def greeting():
    """
    Greets the user upon starting the Survey
    """
    print(
        "Welcome to my Social Media Survey\n"
        "Please take your time, \n"
        "and feel free to answer my questions below: \n"
    )


def name():
    """
    Keep a user inside of a while-loop until
    they give a valid name using alpha.
    """
    while True:
        prompt = (
            "Please enter your name below, \n"
            "it can be full name or "
            "just your first name: \n"
        )
        NAME = input(prompt).strip().title()
        clear()
        if NAME.isalpha():
            return NAME
        else:
            print(f"Sorry, {NAME} is invalid, please use only letters.")


def age(sv_name):
    """
    Keep a user inside of a while-loop
    until they give a valid age using numbers.
    """
    while True:
        AGE = input(f"Welcome {sv_name}, how old are you?\n")
        if AGE.isdigit():
            return int(AGE)
        else:
            print(f"Sorry, {AGE} is invalid, please use only numbers.")


def screen_time(sv_name, sv_age, worksheet):
    """
    Keep a user inside a while-loop that also
    checks all characters for number & decimal input.
    """
    print(
        f"Great! Your name is {sv_name}, and you are {sv_age}.\n"
        "Please share your average screen time daily in hours, \n"
        "this can also include decimals for specificity:\n"
    )

    while True:
        sv_time = input()
        clear()
        if all(char.isdigit() or char == '.' for char in sv_time):
            return sv_time
        else:
            print(
                "Sorry, please enter your screen time, \n"
                "using only numbers and decimal points."
            )


def sv_yesno(prompt):
    """
    Prompts the user during the survey to
    answer only with "Yes" or No" if called.
    """
    while True:
        response = input(prompt).strip().title()
        clear()
        if response in ["Yes", "No"]:
            return response
        else:
            print("Please enter either 'Yes' or 'No'.")


def sv_scale(prompt, min_value, max_value):
    while True:
        try:
            response = int(input(prompt))
            if min_value <= response <= max_value:
                return response
            else:
                print(
                    f"Sorry, please enter a number "
                    "between {min_value} and {max_value}."
                    )
        except ValueError:
            print("Please enter a valid number.")


def sv_question1():
    return sv_yesno(
        "Do you feel like you are spending too much time \n"
        "on Social Media daily? (Yes/No) \n"
    )


def sv_question2():
    return sv_yesno(
        "Do you find yourself feeling the need \n"
        "to be on Social Media often? (Yes/No) \n"
    )


def sv_question3():
    return sv_scale(
        "On a scale of 1 to 10, how frequently \n"
        "do you check for notifications? \n"
        "(1 being rarely, 10 being always): \n",
        1, 10
    )


def sv_question4():
    return sv_scale(
        "On a scale of 1 to 10, how often do you ignore other important \n"
        "activities or responsibilities because of social media use? \n"
        "(1 being rarely, 10 being always): \n",
        1, 10
    )


def sv_question5():
    while True:
        response = input(
            "How often do you find yourself comparing \n"
            "your life to others' on social media?\n"
            "A. Frequently, I often feel like a failure in comparison\n"
            "B. Occasionally, but I try not to let it affect me\n"
            "C. Rarely, I know that people usually show only the\n"
            "best parts of their lives on social media\n"
            "Please choose A, B, or C: \n").strip().upper()
        clear()
        if response in ['A', 'B', 'C']:
            return response
        else:
            print("Please select a valid option (A, B, or C).")


def sv_question6():
    while True:
        response = input(
            "How do you feel when you see others having fun "
            "on social media while you're not included?\n"
            "A. Fear of missing out: I feel left out and envious\n"
            "B. Indifferent: I understand that not "
            "every moment is captured online\n"
            "C. Happy for them: I appreciate their experiences \n"
            "without feeling left out\n"
            "Choose A, B, or C: ").strip().upper()
        clear()
        if response in ['A', 'B', 'C']:
            return response
        else:
            print("Please select a valid option (A, B, or C).")


def sv_analysis(responses):
    """
    Analyse the answers given by the user.
    """
    positive_count = 0
    negative_count = 0
    for response in responses:
        if response in ['Yes', 10, 'A']:
            negative_count += 1
        elif response in ['No', 'B', 'C'] or (isinstance(response, int) and response < 5):  # NOQA
            positive_count += 1

    clear()
    if positive_count > negative_count:
        print(
            "You seem perfectly well with the way you're going, \n"
            "a completely healthy user of social media."
        )
    elif positive_count < negative_count:
        print(
            "From my personal experience, I think you should \n"
            "look into self-improvement for time spent \n"
            "on your social media apps."
        )
    else:
        print(
            "Your answers overall are okay, "
            "your social media use seems balanced."
        )
    print(
        "\nThank you for taking the time to fill out my survey\n"
        "Check back every month for a new survey."
    )


def sv_handle():
    """
    Handles inputs to put into the response once all questions are answered.
    """
    responses = []
    responses.append(sv_question1())
    responses.append(sv_question2())
    responses.append(sv_question3())
    responses.append(sv_question4())
    responses.append(sv_question5())
    responses.append(sv_question6())

    sv_analysis(responses)


def main():
    """
    Runs the survey program with all the functions declared.
    """
    clear()
    greeting()
    sv_name = name()
    sv_age = age(sv_name)

    worksheet = SURVEY_RESULTS_SHEET.sheet1

    sv_time = screen_time(sv_name, sv_age, worksheet)
    svy_question1 = sv_question1()
    svy_question2 = sv_question2()
    svy_question3 = sv_question3()
    svy_question4 = sv_question4()
    svy_question5 = sv_question5()
    svy_question6 = sv_question6()

    worksheet.append_row([
        sv_name, sv_age, sv_time,
        svy_question1, svy_question2,
        svy_question3, svy_question4,
        svy_question5, svy_question6
    ])

    sv_analysis([
        svy_question1, svy_question2,
        svy_question3, svy_question4,
        svy_question5, svy_question6
    ])


main()
