import pandas as pd

class DataAgent:
    def load_data(self, path: str):
        df = pd.read_csv(path)
        return df
