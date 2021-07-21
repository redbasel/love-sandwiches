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
    GET SALES DATA FROM CUSTOMER. runs a whielloop to collct valid string frm user via temrinal.
     mus t 6  nubmers sperated vy commas. loop wil requiest indefintly until tis valid

    """
    while True:

        print('Please enter sales data from te ast market.')
        print('data should be six numbers, seperated by commas.')
        print('Example: 20,30,40,50\n')

        data_str = input('enter your data here:\n')
    
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
    """
def update_sales_worksheet(data):
    """
    """
    Update sales worksheet, add new row with the list data provided.
    """
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print('Sales worksheet updated succesfully.\n')


def update_surplus_worksheet(data):
    """
    """

    Update sales worksheet, add new row with the list data provided.
    """
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print('Surplus worksheet updated succesfully.\n')
    """

def update_worksheet(data, worksheet):
    """
    receive slist of integers ot beisneretd int wkrsheet.
    updates relvenat worksheet wit the dat aprovided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated succesfully\n")



def calculate_surplus_data(sales_row):
    """
    compare sales with previus day

    """
    print("calcaling surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(f"stock row: {stock_row}")
    print(f"sales row: {sales_row}")

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data



    

def get_last_5_entries_sales():
    """
    collects colmns of data frm sales worksheet collectin
    g the last fice netriees for aear columns and returns t eaverage
    """
    sales = SHEET.worksheet("sales")
    #column = sales.col_values(3)
    #print(column)

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns

def calculate_stock_data(data):
    """

    """
    print('calculating stock data...\n')
    new_stock_data=[]

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data



def main():
    """
    Run all program fucntons
    variables define and thenthe functions run with the selected variables
    """


    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")




print('welcome ot love sandwiche sdata autoamtion')
main()

