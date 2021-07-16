import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    GET SALES DATA FROM CUSTOMER. runs a whielloop to collct valid string frm user via temrinal.
     mus t 6  nubmers sperated vy commas. loop wil requiest indefintly until tis valid

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

    return sales_data

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

def update_sales_worksheet(data):
    """

    Update sales worksheet, add new row with the list data provided.

    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print('Sales worksheet updated succesfully.\n')


def calculate_surplus_data(sales_row):
    """
    compare sales with previus day

    """
    print("calcaling surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)
    



def main():
    """
    Run all program fucntons
    """


    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)

print('welcome ot love sandwiche sdata autoamtion')
main()
