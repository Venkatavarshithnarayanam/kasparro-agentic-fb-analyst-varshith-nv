class CreativeGenerator:
    def generate_creatives(self, validated_data):
        insights = validated_data.get("validated_insights", [])
        creatives = []

        for item in insights:
            base = item.get("title", "Ad Creative")

            headline = f"{base} - Improved Version"
            primary_text = "A refined message based on campaign data to improve engagement."
            cta = "Shop Now"

            creatives.append({
                "insight_id": item.get("id", ""),
                "headline": headline,
                "primary_text": primary_text,
                "cta": cta
            })

        return {"creatives": creatives}
