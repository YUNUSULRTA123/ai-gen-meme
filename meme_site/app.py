from flask import Flask, render_template, request, send_file
from meme_generator import generate_meme
from ai_text_gen import generate_meme_text
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['MEME_FOLDER'] = os.path.join(BASE_DIR, 'static', 'memes')
app.config['GENERATED_FOLDER'] = os.path.join(BASE_DIR, 'static', 'generated')

os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    meme_templates = os.listdir(app.config['MEME_FOLDER'])
    generated_meme_path = None
    ai_text = ""

    if request.method == 'POST':
        mode = request.form.get('mode')
        template = request.form.get('template')
        
        if mode == 'manual':
            top_text = request.form.get('top_text')
            bottom_text = request.form.get('bottom_text')
        else:
            topic = request.form.get('topic')
            ai_text = generate_meme_text(topic)
            # Для простоты возьмём AI-текст как верхний и нижний
            top_text = ai_text
            bottom_text = ""

        input_path = os.path.join(app.config['MEME_FOLDER'], template)
        output_filename = f"generated_{template}"
        output_path = os.path.join(app.config['GENERATED_FOLDER'], output_filename)

        generate_meme(input_path, top_text, bottom_text, output_path)
        generated_meme_path = output_path

    return render_template('index.html', memes=meme_templates, generated_meme=generated_meme_path, ai_text=ai_text)

@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join(app.config['GENERATED_FOLDER'], filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
