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
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)

def get_sales_data():
    """
    GET SALES DATA FROM CUSTOMER

    """
    print('Please enter sales data from te ast market.')
    print('data should be six numbers, seperated by commas.')
    print('Example: 20,30,40,50')

    data_str = input('enter your data here')
    print(f"The data provided is{data_str}")

get_sales_data()
