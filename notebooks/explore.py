import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    df = pd.read_csv("data/sales.csv")
    df["total_revenue"] = df["quantity_sold"] * df["price"]
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    return df


def revenue_by_branch(df):
    return df.groupby("branch")["total_revenue"].sum()


def quantity_by_product(df):
    return df.groupby("product")["quantity_sold"].sum().sort_values()


def revenue_by_month(df):
    return df.groupby("month")["total_revenue"].sum()


def plot_revenue_by_branch(df):
    data = revenue_by_branch(df)
    fig, ax = plt.subplots()
    sns.barplot(x=data.index, y=data.values, ax=ax)
    ax.set_title("Revenue by Branch")
    ax.set_xlabel("Branch")
    ax.set_ylabel("Total Revenue")
    return fig


def plot_quantity_by_product(df):
    data = quantity_by_product(df)
    fig, ax = plt.subplots()
    sns.barplot(x=data.values, y=data.index, ax=ax)
    ax.set_title("Quantity Sold by Product (slowest first)")
    ax.set_xlabel("Quantity Sold")
    ax.set_ylabel("Product")
    return fig


def plot_revenue_by_month(df):
    data = revenue_by_month(df)
    fig, ax = plt.subplots()
    sns.lineplot(x=data.index, y=data.values, marker="o", ax=ax)
    ax.set_title("Revenue by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Revenue")
    return fig


if __name__ == "__main__":
    df = load_data()

    print("=== Revenue by branch ===")
    print(revenue_by_branch(df))

    print("\n=== Quantity sold by product (slowest first) ===")
    print(quantity_by_product(df))

    print("\n=== Revenue by month ===")
    print(revenue_by_month(df))

    plot_revenue_by_branch(df).savefig("data/revenue_by_branch.png")
    plot_quantity_by_product(df).savefig("data/quantity_by_product.png")
    plot_revenue_by_month(df).savefig("data/revenue_by_month.png")
    print("\nCharts saved to data/ folder.")
