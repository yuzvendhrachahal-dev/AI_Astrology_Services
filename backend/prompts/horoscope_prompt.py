def horoscope_prompt(name: str, birth_info: dict) -> str:
    """Return a prompt string for generating a horoscope for the given birth info."""
    return f"Generate a concise horoscope for {name} given birth data: {birth_info}."
