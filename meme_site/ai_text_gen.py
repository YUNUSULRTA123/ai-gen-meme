import os
import google.generativeai as genai
import re

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

def extract_first_meme_text(response_text):
    match = re.search(r'\*+\s+\*\*Текст:\*\*\s*(.+)', response_text)
    if match:
        return match.group(1).strip()
    return response_text.strip()

def generate_meme_text(topic):
    prompt = f"""
Ты — весёлый и остроумный помощник. Придумай короткий смешной мем на тему: {topic}.
Дай 3 варианта, каждый начинай с **Текст:**
"""
    try:
        response = model.generate_content(prompt)
        print("[Gemini ответ]:", response.text)
        return extract_first_meme_text(response.text)
    except Exception as e:
        print("[Gemini Error]:", e)
        return "Ошибка генерации текста."
