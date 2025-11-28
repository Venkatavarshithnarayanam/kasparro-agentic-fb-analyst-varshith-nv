import numpy as np

class InsightAgent:
    def generate_insights(self, data):
        df = data["df"]
        summary = data["summary"]

        insights = []

        if "ctr" in df.columns:
            avg_ctr = summary.get("avg_ctr", 0)
            high_ctr_ads = df.nlargest(3, "ctr")[["ctr"]]
            low_ctr_ads = df.nsmallest(3, "ctr")[["ctr"]]

            insights.append({
                "id": "insight_ctr_overall",
                "title": "Click-through rate performance overview",
                "details": f"Average CTR is {round(avg_ctr * 100, 2)}%.",
                "high_performers": high_ctr_ads["ctr"].round(4).tolist(),
                "low_performers": low_ctr_ads["ctr"].round(4).tolist()
            })

        if "cpc" in df.columns:
            avg_cpc = summary.get("avg_cpc", 0)
            insights.append({
                "id": "insight_cpc_cost",
                "title": "Cost-per-click analysis",
                "details": f"Average CPC is ₹{round(avg_cpc, 2)}.",
            })

        if "conversion_rate" in df.columns:
            avg_cr = summary.get("avg_conversion_rate", 0)
            high_cr_ads = df.nlargest(3, "conversion_rate")[["conversion_rate"]]

            insights.append({
                "id": "insight_conversion",
                "title": "Conversion rate patterns",
                "details": f"Average conversion rate is {round(avg_cr * 100, 2)}%.",
                "top_conversion_rates": high_cr_ads["conversion_rate"].round(4).tolist()
            })

        if "cpm" in df.columns:
            avg_cpm = summary.get("avg_cpm", 0)
            insights.append({
                "id": "insight_cpm",
                "title": "Cost-per-mille evaluation",
                "details": f"Average CPM is ₹{round(avg_cpm, 2)}."
            })

        return {"insights": insights}
