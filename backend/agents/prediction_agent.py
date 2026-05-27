from services.openai_service import ask_openai

async def birthstar_analysis(star):

    prompt=f"""

Generate:

Personality
Strengths
Weaknesses
Career

Birthstar:

{star}

"""

    return await ask_openai(prompt)