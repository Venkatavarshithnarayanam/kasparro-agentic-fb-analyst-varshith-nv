class InsightAgent:
    def generate_insights(self, data):
        insights = {
            "insights": [
                "Basic data load successful.",
                f"Dataset contains {len(data)} rows."
            ]
        }
        return insights
