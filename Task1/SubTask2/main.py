import pandas as pd
from pathlib import Path


def target_change():
    dir = Path(__file__).parent.parent
    df = pd.read_csv(dir / "sales_target.csv")

    # get the data from the furniture category
    furniture = df[df["Category"] == "Furniture"].copy()

    # converting the column to datetime
    furniture["Month of Order Date"] = pd.to_datetime(
        furniture["Month of Order Date"]
    )

    # sorting it from january up to december
    furniture = furniture.sort_values("Month of Order Date")

    furniture["Percentage Change"] = (
        furniture["Target"].pct_change() * 100
    )

    return furniture


if __name__ == "__main__":
    result = target_change()
    print(result)