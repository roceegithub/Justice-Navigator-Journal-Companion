import justice_navigator_info
import pandas as pd
import numpy as np
import os
import datetime
from colorama import init, Fore, Back, Style      # type: ignore   
import colorama                                   # type: ignore

autoreset=True

def welcome_message():
    """introduction to journal"""
    print(f"\n{"="*14} Welcome to your Journal Companion {"="*15}\n")
    print(f"This is a private space to reflect on your journey.")
    print(f"All entries will be securely saved on your device.")
    print(f"Take your time, there's no rush.\n")

def user_info():
    """capture basic information from user"""
    print(f"As we begin this journey, let's get to know some more ...")

    # capture user name with validation
    while True:
        name = input("What is your first name, or what would like to be addressed as? ").strip()
        if name:
            break
        else:
            print(f"Please enter you name to continue.")

    # date capture for time stamps
    while True:
        reentry_date = input("When did you reenter society? (MM/DD/YYYY) ")
        try:
            datetime.datetime.strptime(reentry_date, "%m/%d/%Y")
            break
        except ValueError:
            print(f"Please enter a valid date in MM/DD/YYYY format.")

    return name, reentry_date

def daily_reflection(name):
    """guide user through daily reflection"""
    print(f"\n Hello {name}, let's reflect on today...")

    # record date and time
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    print(f"\nToday's Date: {current_date}")
    print(f"Current Time: {current_time}")

    # need to evaluate the daily questions with team, these are possible examples
    questions = [
        "What's a positive thing that happened today?",
        "What made the day challenging, and how did you handle it?",
        "Did you connect with anyone today, how was that experience?",
        "What did you learn about yourself today?",
        "Is there is something that you are looking forward to tomorrow?",
        "What would you do differently tomorrow? ",
        "How are you feeling at this moment? (use 1-5 words)"
    ]

    # blank space for response
    answers = []

    for e, question in enumerate(questions, 1):
        print(f"\n{e}. {question}")
        answer = input("Let me hear your thoughts: ")
        answers.append(answer)

        # user control to skip questions
        if e < len(questions):
            skip = input("\nPress ENTER to continue or type 'SKIP' to finish: ")
            if skip.lower() == 'SKIP':
                # if SKIP, fill in the rest of the questions with "Skipped"
                for s in range(e, len(questions)):
                    answers.append("Skipped")
                break

    return current_date, current_time, answers

def weekly_check_in(name):
    """Weekly checkin with deeper questions"""
    print("\n{name}, let's check-in...")

    questions = [
        "What do you feel was your biggest accomplishment this week? ",
        "What do you feel was the most challenging this week? ",
        "What support do you need right now? ",
        "What is one goal you would like to set for next week? ",
        "How have you grown of changed this week? "
    ]

    answers = []
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")

    for question in questions:
        print("\n{question}")
        answer = input("Your response: ")
        answers.append(answer)

    return current_date, answers

def save_entry(entry_type, date, time, content, name):
    """Create file for Journal Entries"""
    filename = f"{name}_{date}_journal.txt"

    with open(filename, "a") as file:
        file.write(f"\n{'='*64}")
        file.write(f"Entry Type: {entry_type}")
        file.write(f"Date: {date} | Time: {time}")
        file.write(f"{'='*64}\n")

        if entry_type == "Daily Reflection":
            questions = [
                "Positive moment: ",
                "Challenge handled: ",
                "Connections: ",
                "Self-discovery: ",
                "Looking forward: ",
                "Do differently: ",
                "Current feelings: "
            ]

            for e, (question, answer) in enumerate(zip(questions, content)):
                file.write(f"{question}{answer}\n")

        elif entry_type == "Weekly Check-in":
            questions = [
                "Biggest accomplishment: ",
                "Most challenging: ",
                "Support needed: ",
                "Goal for next week: ",
                "Personal goal: "
            ]