from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    MODEL_NAME
)

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def ask_openai(prompt):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        response_format={
        "type":"json_object"
    },

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content