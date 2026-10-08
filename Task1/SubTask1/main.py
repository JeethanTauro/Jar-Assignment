import pandas as pd
from pathlib import Path

#find the total sales amount grouped by category
def total_sales_per_category(dataframe):
    total_sales_per_category = dataframe.groupby('Category')['Amount'].sum()
    return total_sales_per_category

#for each category, find the average profit per order, profit margin as percentage of Amount
def average_profit_and_margin(dataframe):
    result = dataframe.groupby('Category').agg(
        average_profit = ("Profit","mean"),
        total_amount = ("Amount","sum"),
        total_profit = ("Profit",sum)
    )
    print(type(result))
    result["profit_margin"] = (result["total_profit"] / result["total_amount"]) * 100

    return result


if __name__ == "__main__":
    dir = Path(__file__).parent.parent
    dataframe = pd.read_csv(dir / "merged_list_of_orders_and_order_details.csv")


    total_sales_per_category = total_sales_per_category(dataframe)
    print(total_sales_per_category)


    average_profit_and_margin = average_profit_and_margin(dataframe)
    print(average_profit_and_margin)