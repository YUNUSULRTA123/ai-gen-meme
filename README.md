# 🧠 MemeGen — AI Генератор Мемов

Генератор мемов на Flask с автогенерацией смешного текста с помощью Gemini и наложением текста на изображение. Поддержка логотипа Trollface 🧌


---

## 🚀 Возможности

- 🤖 Генерация текста с Gemini по теме
- 🖼️ Генерация мема (изображение + текст)
- 🧠 Пользователь вводит тему → AI пишет смешной текст
- 🎨 Троллфейс логотип
- 🌐 Простой веб-интерфейс (Flask)

---

## 📁 Структура проекта

```
meme_site/
├── static/
│ ├── css/
│ │ └── style.css
│ ├── img/
│ │ └── trollface.svg
│ └── memes/ 
├── templates/
│ └── index.html
├── ai_text_gen.py 
├── meme_generator.py 
├── app.py 
├── requirements.txt
└── README.md
```

---
## ⚙️ Установка

### 1. Установи зависимости:

```
pip install -r requirements.txt
```
### 2. Получи API-ключ Gemini: 
<https://ai.google.dev/>
