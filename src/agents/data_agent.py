import pandas as pd

class DataAgent:
    def load_data(self, path: str):
        df = pd.read_csv(path)

        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        if "clicks" in df.columns and "impressions" in df.columns:
            df["ctr"] = (df["clicks"] / df["impressions"]).fillna(0)

        if "spend" in df.columns and "clicks" in df.columns:
            df["cpc"] = (df["spend"] / df["clicks"]).replace([float("inf")], 0).fillna(0)

        if "spend" in df.columns and "impressions" in df.columns:
            df["cpm"] = ((df["spend"] / df["impressions"]) * 1000).fillna(0)

        if "conversions" in df.columns and "clicks" in df.columns:
            df["conversion_rate"] = (df["conversions"] / df["clicks"]).fillna(0)

        if "revenue" in df.columns and "spend" in df.columns:
            df["roas"] = (df["revenue"] / df["spend"]).replace([float("inf")], 0).fillna(0)

        summary = {
            "total_rows": len(df),
            "avg_ctr": float(df["ctr"].mean()) if "ctr" in df.columns else None,
            "avg_cpc": float(df["cpc"].mean()) if "cpc" in df.columns else None,
            "avg_cpm": float(df["cpm"].mean()) if "cpm" in df.columns else None,
            "avg_conversion_rate": float(df["conversion_rate"].mean()) if "conversion_rate" in df.columns else None
        }

        return {"df": df, "summary": summary}
