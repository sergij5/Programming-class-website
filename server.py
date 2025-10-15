from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__, static_folder='.', template_folder='.')

PORT = 8000

print("=" * 50)
print("🚀 Запускаем Flask сервер...")
print(f"📁 Текущая папка: {os.getcwd()}")
print(f"🌐 Сервер будет доступен по: http://localhost:{PORT}")
print("=" * 50)

# Главная страница
@app.route('/')
def index():
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    else:
        return "<h1>❌ Файл index.html не найден</h1>"

# Раздача статических файлов (css, js и т.д.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    try:
        app.run(port=PORT)
    except OSError:
        print(f"❌ Порт {PORT} занят! Попробуй другой порт.")
