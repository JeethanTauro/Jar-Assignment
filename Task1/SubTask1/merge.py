
#merge the list_of_orders and order_details on the key 'Order ID'

import pandas as pd
from pathlib import Path



#merges the two csv files and creates a new file
def merge():
    dir = Path(__file__).parent.parent
    list_of_orders_path = dir / "list_of_orders.csv"
    order_details_path = dir / "order_details.csv"

    list_of_orders_df = pd.read_csv(list_of_orders_path)
    order_details_df = pd.read_csv(order_details_path)

    merged_df   = pd.merge(list_of_orders_df, order_details_df, on='Order ID')
    merged_df.to_csv(Path(__file__).parent / "merged_list_of_orders_and_order_details.csv",index=False)


if __name__ == "__main__":
    merge()


