import pandas as pd
from ..logging_config import get_logger

logger = get_logger(__name__)

EXPECTED_COLUMNS = [
    "campaign_id", "impressions", "clicks",
    "spend", "conversions", "revenue", "date"
]

class DataAgent:

    def load_data(self, path: str):
        logger.info(f"DataAgent: Starting to load dataset from {path}")

        df = None

        # Retry mechanism (3 attempts)
        for attempt in range(1, 4):
            try:
                df = pd.read_csv(path)
                logger.info(f"DataAgent: File loaded successfully on attempt {attempt}")
                break
            except Exception as e:
                logger.error(f"DataAgent: Failed to load data (attempt {attempt}) - {e}")
                if attempt == 3:
                    raise e  # final failure

       
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

       
        missing = set(EXPECTED_COLUMNS) - set(df.columns)
        extra = set(df.columns) - set(EXPECTED_COLUMNS)

        if missing:
            logger.warning(f"DataAgent: Missing columns: {missing}")
        if extra:
            logger.info(f"DataAgent: Extra columns present: {extra}")

       
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

        logger.info(f"DataAgent: Loaded {summary['total_rows']} rows with metrics summary: {summary}")

        return {"df": df, "summary": summary}
