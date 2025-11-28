import json
import os
from agents.planner import Planner
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.evaluator import Evaluator
from agents.creative_generator import CreativeGenerator
from logging_config import get_logger

logger = get_logger(__name__)

def main():
    logger.info("🚀 Pipeline Started")

    planner = Planner()
    data_agent = DataAgent()
    insight_agent = InsightAgent()
    evaluator = Evaluator()
    creative_gen = CreativeGenerator()

   
    task = "Analyze Facebook Ads Performance"
    plan = planner.plan(task)
    logger.info(f"Plan: {plan}")

   
    data = data_agent.load_data("data/synthetic_fb_ads_undergarments.csv")

   
    insights = insight_agent.generate_insights(data)

    validated = evaluator.evaluate(insights)

    creatives = creative_gen.generate_creatives(validated)

    os.makedirs("reports", exist_ok=True)

    with open("reports/insights.json", "w") as f:
        json.dump(validated, f, indent=2)
    logger.info("Saved insights.json")

    with open("reports/creatives.json", "w") as f:
        json.dump(creatives, f, indent=2)
    logger.info("Saved creatives.json")


    metrics = {
        "rows_processed": data["summary"]["total_rows"],
        "num_insights": len(validated.get("validated_insights", [])),
        "num_creatives": len(creatives.get("creatives", []))
    }

    with open("reports/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    logger.info(f"Saved metrics.json → {metrics}")
    logger.info("🎉 Pipeline Completed Successfully")


if __name__ == "__main__":
    main()
