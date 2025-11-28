from ..logging_config import get_logger

logger = get_logger(__name__)

class Evaluator:
    def evaluate(self, insights: dict) -> dict:
        """
        Evaluates insights and adds a simple confidence score.
        """
        logger.info("Evaluator: Starting evaluation of insights...")

        raw_insights = insights.get("insights", [])
        validated = []

        if not raw_insights:
            logger.warning("Evaluator: No insights received for evaluation.")
            return {"validated_insights": []}

        for ins in raw_insights:
            value = ins.get("value", 0)

            # Simple confidence score logic
            if value > 0:
                confidence = min(1.0, value * 10)
            else:
                confidence = 0.1  # fallback low confidence

            validated_insight = {
                "type": ins.get("type"),
                "detail": ins.get("detail"),
                "value": value,
                "confidence": round(confidence, 4)
            }

            validated.append(validated_insight)
            logger.info(f"Evaluator: Evaluated {ins['type']} → confidence {confidence}")

        logger.info(f"Evaluator: Completed evaluation of {len(validated)} insights")

        return {"validated_insights": validated}
