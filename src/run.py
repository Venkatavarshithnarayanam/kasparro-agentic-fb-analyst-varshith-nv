import json
from agents.planner import Planner
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.evaluator import Evaluator
from agents.creative_generator import CreativeGenerator

def main():
    task = "Analyze Facebook Ads Performance"

    planner = Planner()
    data_agent = DataAgent()
    insight_agent = InsightAgent()
    evaluator = Evaluator()
    creative_gen = CreativeGenerator()

    plan = planner.plan(task)

    data = data_agent.load_data("data/synthetic_fb_ads_undergarments.csv")

    insights = insight_agent.generate_insights(data)

    validated = evaluator.evaluate(insights)

    with open("reports/insights.json", "w") as f:
        json.dump(validated, f, indent=4)

    creatives = creative_gen.generate_creatives(validated)

    with open("reports/creatives.json", "w") as f:
        json.dump(creatives, f, indent=4)

    print("Pipeline completed. Outputs saved in the reports folder.")

if __name__ == "__main__":
    main()
