from ..logging_config import get_logger

logger = get_logger(__name__)

class CreativeGenerator:
    def generate_creatives(self, insights: dict) -> dict:
        """
        Generates simple creative suggestions based on insights.
        """
        logger.info("CreativeGenerator: Starting creative generation...")

        validated_insights = insights.get("validated_insights", [])

        if not validated_insights:
            logger.warning("CreativeGenerator: No validated insights available. Returning empty creatives.")
            return {"creatives": []}

        creatives = []

        for ins in validated_insights:
            insight_type = ins.get("type", "Unknown")
            confidence = ins.get("confidence", 0)

            creative_text = f"Suggested creative for {insight_type}: Focus on improving this metric using high CTR visuals, clear CTA, and optimized targeting."
            
            creative_item = {
                "insight_type": insight_type,
                "confidence": confidence,
                "creative": creative_text
            }

            creatives.append(creative_item)
            logger.info(f"CreativeGenerator: Created creative for {insight_type} (confidence: {confidence})")

        logger.info(f"CreativeGenerator: Finished generating {len(creatives)} creatives")

        return {"creatives": creatives}
