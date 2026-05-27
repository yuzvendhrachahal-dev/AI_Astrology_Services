class CompatibilityAgent:
    """Agent responsible for computing compatibility between two birth charts."""

    def __init__(self, services=None):
        self.services = services

    def run(self, data: dict) -> dict:
        # TODO: implement astrology logic or call LLM orchestrator
        return {"result": "compatibility_stub", "input": data}
