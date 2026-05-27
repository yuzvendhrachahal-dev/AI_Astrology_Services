def birthstar_prompt(name: str, birth_info: dict) -> str:
    """Return a prompt string for computing birth star / nakshatra style insights."""
    return f"Analyze birth star for {name} with data: {birth_info}. Provide short insights."
