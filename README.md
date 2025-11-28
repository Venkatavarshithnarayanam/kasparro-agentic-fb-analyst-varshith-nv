# Kasparro – Agentic FB Ads Performance Analyst

This repository contains my submission for the Applied AI Engineer assignment at Kasparro.  
The goal of this project is to design a small agent-based pipeline that analyses a Facebook Ads dataset, generates data-backed insights, evaluates them, and produces creative recommendations.

---

## 1. Project Overview

The solution follows a simple, modular structure using lightweight agents:

- **Planner** – breaks down the analysis task.
- **DataAgent** – loads the CSV dataset and computes key performance metrics.
- **InsightAgent** – generates structured insights based on the data.
- **Evaluator** – validates insights using simple quantitative checks.
- **CreativeGenerator** – produces basic creative ideas linked to each insight.

The final outputs are stored in the `reports/` directory.

---

## 2. Repository Structure

📁 kasparro-agentic-fb-analyst-varshith-nv
┣ 📁 src
┃ ┣ 📁 agents
┃ ┃ ┣ 📄 planner.py
┃ ┃ ┣ 📄 data_agent.py
┃ ┃ ┣ 📄 insight_agent.py
┃ ┃ ┣ 📄 evaluator.py
┃ ┃ ┗ 📄 creative_generator.py
┃ ┗ 📄 run.py
┣ 📁 prompts
┃ ┣ 📄 planner_base.txt
┃ ┣ 📄 insight_base.txt
┃ ┗ 📄 creative_base.txt
┣ 📁 reports
┃ ┣ 📄 insights.json
┃ ┣ 📄 creatives.json
┃ ┗ 📄 report.md
┣ 📁 data
┃ ┗ 📄 synthetic_fb_ads_undergarments.csv
┣ 📁 config
┃ ┗ 📄 config.yaml
┗ 📄 requirements.txt

## 4. Output Files

- **insights.json** – structured insights extracted from the dataset  
- **creatives.json** – simple creative ideas derived from insights  
- **report.md** – written summary of key findings and recommendations  

These represent the final deliverables for the assignment.

---

## 5. Notes

- The dataset used is the provided `synthetic_fb_ads_undergarments.csv`.
- The code is intentionally minimal and clear to highlight reasoning steps and agent modularity.
- No external AI or LLM services are used in this version to keep the pipeline deterministic and easy to run.

---

## 6. Author
**Varshith N V**  
Applied AI Engineer Assignment Submission


