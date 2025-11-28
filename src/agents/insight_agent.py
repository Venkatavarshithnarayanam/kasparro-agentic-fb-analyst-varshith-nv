from ..logging_config import get_logger

logger = get_logger(__name__)

class InsightAgent:
    def generate_insights(self, data: dict) -> dict:
        """
        Generates simple structured insights based on dataframe metrics.
        """
        logger.info("InsightAgent: Generating insights...")

        df = data.get("df")

        if df is None or df.empty:
            logger.warning("InsightAgent: Received empty dataframe, returning empty insights.")
            return {"insights": []}

        insights = []

        # CTR Insight
        if "ctr" in df.columns:
            avg_ctr = float(df["ctr"].mean())
            insights.append({
                "type": "CTR",
                "detail": f"Average CTR: {avg_ctr:.4f}",
                "value": avg_ctr
            })
            logger.info(f"InsightAgent: CTR insight generated → {avg_ctr}")

        # CPC Insight
        if "cpc" in df.columns:
            avg_cpc = float(df["cpc"].mean())
            insights.append({
                "type": "CPC",
                "detail": f"Average CPC: {avg_cpc:.4f}",
                "value": avg_cpc
            })
            logger.info(f"InsightAgent: CPC insight generated → {avg_cpc}")

        # ROAS Insight
        if "roas" in df.columns:
            avg_roas = float(df["roas"].mean())
            insights.append({
                "type": "ROAS",
                "detail": f"Average ROAS: {avg_roas:.4f}",
                "value": avg_roas
            })
            logger.info(f"InsightAgent: ROAS insight generated → {avg_roas}")

        logger.info(f"InsightAgent: Finished generating {len(insights)} insights")
        return {"insights": insights}
