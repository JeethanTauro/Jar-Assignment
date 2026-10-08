'''
Decide to use a programatic way to convert excel files into CSV files instead of third party websites because I am assuming
the data is confidential and propreitory
'''

import pandas as pd
from pathlib import Path



# this is the function to convert the excel files into csv files
def convert_to_csv(path : str, file_name:str):
    dataframe = pd.read_excel(path)

    dataframe.to_csv(f"{file_name}.csv", index=False, header=True)



if __name__ == "__main__":

    #path of the excel files
    project_dir = Path(__file__).parent.parent

    list_of_orders_path = project_dir / "List_of_Orders.xlsx"
    order_details_path = project_dir / "Order_Details.xlsx"
    sales_target_path = project_dir / "Sales_target.xlsx"


    convert_to_csv(list_of_orders_path, "list_of_orders")
    convert_to_csv(order_details_path, "order_details")
    convert_to_csv(sales_target_path, "sales_target")