import pandas as pd
from pathlib import Path


REQUIRED_COLUMNS = {"date", "description", "category", "type", "amount"}


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> pd.DataFrame:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        if self.file_path.suffix == ".csv":
            df = pd.read_csv(self.file_path)
        elif self.file_path.suffix in [".xlsx", ".xls"]:
            df = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")

        self._validate_columns(df)
        return df

    def _validate_columns(self, df: pd.DataFrame):
        missing = REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")