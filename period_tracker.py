from dotenv import load_dotenv
#from pprint import pprint
import os
import requests

load_dotenv()

def calculate_next_period(date: str) -> str:
    #Format should be DD-MM-YYYY
    return '25-06-2025'

def get_username() -> str:
    username = input('Enter ur name: ').strip()
    while len(username) <= 0:
        username = input('Name cannot be empty!\nEnter ur name: ').strip()
    return username

def get_period_date() -> str:
    date = input('Enter the date of your last period (DD-MM-YYYY)')

if __name__ == "__main__":
    print("\n*** Running Period Tracker ***\n")
