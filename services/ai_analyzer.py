# This is the gemini analyzer code

# import os
# import httpx

# API_KEY = os.getenv("GEMINI_API_KEY")

# async def analyze_with_gemini(text: str, sector: str) -> str:

#     prompt = f"""
# You are a financial market analyst.

# Provide a concise Indian market analysis for the {sector} sector including:
# - current trends
# - trade opportunities
# - export potential
# - government initiatives
# """

#     if API_KEY:
#         try:
#             url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
#             payload = {"contents": [{"parts": [{"text": prompt}]}]}

#             async with httpx.AsyncClient(timeout=20) as client:
#                 r = await client.post(url, json=payload)
#                 data = r.json()

#                 if "candidates" in data:
#                     return data["candidates"][0]["content"]["parts"][0]["text"]
#         except:
#             pass

#     # 🧠 Fallback AI Engine
#     return f"""
# The Indian {sector} sector is witnessing steady growth driven by increased domestic demand and supportive government policies.

# Major trade opportunities include export expansion, manufacturing localization, and technology modernization.

# India is becoming a global supplier in this sector, making it attractive for foreign investment and trade partnerships.
# """



# This is the mistral analyzer code from hugging face that i have implemented because gemini is not providing free tier anymore <--------------------------------
import os, httpx

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL}"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

async def analyze_with_ai(text: str, sector: str) -> str:
    prompt = f"""
You are an Indian market analyst.
Using the following news headlines, provide trade opportunity insights for {sector} sector in India.

{text}

Include market overview, opportunities, export potential and risks.
"""

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 350},
        "options": {"wait_for_model": True}
    }

    async with httpx.AsyncClient(timeout=90) as client:
        r = await client.post(API_URL, headers=headers, json=payload)
        data = r.json()

        if isinstance(data, dict) and data.get("error"):
            return f"AI service error: {data['error']}"

        return data[0]["generated_text"]
