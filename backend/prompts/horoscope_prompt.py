def horoscope_prompt(data):

    return f"""
You are a Vedic Astrology Marriage Matching Engine.

INPUT:

Groom:
Name: {data.groom_name}
DOB: {data.groom_dob}
Time: {data.groom_time}
Location: {data.groom_location}

Bride:
Name: {data.bride_name}
DOB: {data.bride_dob}
Time: {data.bride_time}
Location: {data.bride_location}

Generate ONLY valid JSON.

Schema:

{{
 "BoyNakshatra":"",
 "BoyZodiac":"",
 "GirlNakshatra":"",
 "GirlZodiac":"",
 "BoyLagna":"",
 "GirlLagna":"",
 "TotalValue":0,

 "Dhina": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Gana": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Mahendra": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "StreeDeerga": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Yoni": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Rasi": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Rasiyathipaty": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Vasya": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Rajju": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Nadi": {{
   "CompatibilityName":"",
   "Status":"",
   "StatusDescription":""
 }},

 "Summary":""
}}

Return JSON only.
Return clean formatted text.
"""

