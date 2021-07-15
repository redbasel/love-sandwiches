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
    while True:

        print('Please enter sales data from te ast market.')
        print('data should be six numbers, seperated by commas.')
        print('Example: 20,30,40,50')

        data_str = input('enter your data here')
    
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print('Data is valid!')
            break

def validate_data(values):
    """
    Inside the tr, converts all stirng vlae sto integers.
    raises valeerror if strngs cannot be converted into int. or
    if thera are exactly 6 values.
    """

    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False
    
    return True




get_sales_data()
