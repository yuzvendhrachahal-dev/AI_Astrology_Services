def build_horoscope_prompt(data):

    return f"""
You are an experienced Vedic Astrology Marriage Matching Expert.

GROOM

Name: {data.groom_name}
DOB: {data.groom_dob}
Time: {data.groom_time}
Country: {data.groom_country}
Location: {data.groom_location}

BRIDE

Name: {data.bride_name}
DOB: {data.bride_dob}
Time: {data.bride_time}
Country: {data.bride_country}
Location: {data.bride_location}

Generate:

1. Horoscope Matching Summary
2. Compatibility Overview
3. Relationship Strengths
4. Potential Challenges
5. Marriage Guidance
6. Compatibility Rating (Low / Average / Good / Excellent)

Return clean formatted text.
"""