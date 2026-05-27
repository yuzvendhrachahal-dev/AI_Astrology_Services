def naming_prompt(preferences: dict) -> str:
    """Return a prompt string for generating name suggestions based on preferences."""
    return f"Suggest baby names matching preferences: {preferences}. Provide 10 options with short notes."
