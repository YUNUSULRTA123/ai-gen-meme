# 🧠 MemeGen — AI Генератор Мемов

Генератор мемов на Flask с автогенерацией смешного текста с помощью Gemini и наложением текста на изображение. Поддержка логотипа Trollface 🧌

![Trollface](static/img/trollface.svg)

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
│ └── memes/ # Картинки-мемы
├── templates/
│ └── index.html
├── ai_text_gen.py # Генерация текста через Gemini
├── meme_generator.py # Создание изображения
├── app.py # Flask-приложение
├── requirements.txt
└── README.md
```
