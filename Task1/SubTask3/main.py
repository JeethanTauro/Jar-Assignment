import pandas as pd
from pathlib import Path

def top_states():
    dir = Path(__file__).parent.parent
    df = pd.read_csv(dir / "merged_list_of_orders_and_order_details.csv")

    # counting the orders of each state
    order_count = (
        df.groupby("State")["Order ID"]
        .nunique()
        .sort_values(ascending=False)
    )

    #get the top 5 states
    top_5_states = order_count.head(5).index

    # create dataframe of states present in top 5 states
    top_5_df = df[df["State"].isin(top_5_states)]

    result = (
        top_5_df.groupby("State")
        .agg(
            order_count=("Order ID", "nunique"),
            total_sales=("Amount", "sum"),
            average_profit=("Profit", "mean")
        )
        .sort_values("order_count", ascending=False)
    )

    return result

if __name__ == "__main__":
    results  = top_states()
    print(results)