import pandas as pd


class FinancialProcessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self._prepare_data()

    def _prepare_data(self):
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df["amount"] = self.df["amount"].astype(float)

    def total_income(self):
        return self.df[self.df["type"] == "income"]["amount"].sum()

    def total_expense(self):
        return self.df[self.df["type"] == "expense"]["amount"].sum()

    def net_profit(self):
        return self.total_income() - self.total_expense()

    def expenses_by_category(self):
        expenses = self.df[self.df["type"] == "expense"]
        return expenses.groupby("category")["amount"].sum().sort_values(ascending=False)

    def summary(self):
        return {
            "Total Income": self.total_income(),
            "Total Expense": self.total_expense(),
            "Net Profit": self.net_profit(),
        }