from prompts.horoscope_prompt import (
    build_horoscope_prompt
)

from services.openai_service import (
    ask_openai
)


def horoscope_matching_agent(data):

    prompt = build_horoscope_prompt(data)

    result = ask_openai(prompt)

    return result