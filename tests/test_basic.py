from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator import Evaluator
import pandas as pd

def test_data_agent_loads_dataframe():
    """Ensures DataAgent can load a small in-memory dataframe"""
    df = pd.DataFrame({
        "campaign_id": [1],
        "impressions": [100],
        "clicks": [5],
        "spend": [20],
        "conversions": [1],
        "revenue": [80],
        "date": ["2025-01-01"]
    })

    # Save temporary CSV
    df.to_csv("temp_test.csv", index=False)

    agent = DataAgent()
    out = agent.load_data("temp_test.csv")

    assert out["summary"]["total_rows"] == 1

def test_insight_agent_empty_df():
    agent = InsightAgent()
    out = agent.generate_insights({"df": pd.DataFrame(), "summary": {}})
    assert "insights" in out

def test_evaluator_confidence():
    agent = Evaluator()
    sample = {"insights": [{"type": "CTR", "detail": "test", "value": 0.02}]}
    out = agent.evaluate(sample)
    assert out["validated_insights"][0]["confidence"] > 0
