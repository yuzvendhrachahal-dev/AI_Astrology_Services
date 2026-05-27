from agents.prediction_agent import PredictionAgent
from agents.compatibility_agent import CompatibilityAgent
from agents.naming_agent import NamingAgent

class Orchestrator:
    """Simple orchestrator to coordinate agents and services."""

    def __init__(self, services=None):
        self.services = services
        self.prediction = PredictionAgent(services=services)
        self.compatibility = CompatibilityAgent(services=services)
        self.naming = NamingAgent(services=services)

    def run_prediction(self, data: dict) -> dict:
        return self.prediction.run(data)

    def run_compatibility(self, data: dict) -> dict:
        return self.compatibility.run(data)

    def run_naming(self, data: dict) -> dict:
        return self.naming.run(data)
