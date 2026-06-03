import json

from prompts.horoscope_prompt import (
    horoscope_prompt
)

from services.openai_service import (
    ask_openai
)


def horoscope_matching_agent(data):

    prompt = horoscope_prompt(data)

    result = ask_openai(prompt)

    return json.loads(result)