import numpy as np

class Evaluator:
    def evaluate(self, insights_data):
        insights = insights_data.get("insights", [])
        validated = []

        for item in insights:
            confidence = 0.0

            if "details" in item and isinstance(item["details"], str):
                if any(char.isdigit() for char in item["details"]):
                    confidence += 0.4

            if "high_performers" in item and item.get("high_performers"):
                confidence += 0.3

            if "low_performers" in item and item.get("low_performers"):
                confidence += 0.3

            if confidence > 1:
                confidence = 1

            item["confidence"] = round(confidence, 2)
            validated.append(item)

        return {"validated_insights": validated}
