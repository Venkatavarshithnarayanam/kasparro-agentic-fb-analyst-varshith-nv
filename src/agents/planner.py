from ..logging_config import get_logger

logger = get_logger(__name__)

class Planner:
    def plan(self, task: str) -> dict:
        """
        Creates a simple step-by-step plan for the pipeline.
        """
        logger.info(f"Planner: Received task → {task}")

        plan = {
            "task": task,
            "steps": [
                "load_data",
                "extract_metrics",
                "generate_insights",
                "evaluate_insights",
                "generate_creatives"
            ]
        }

        logger.info(f"Planner: Generated {len(plan['steps'])} subtasks")

        return plan
