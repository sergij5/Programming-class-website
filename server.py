import http.server
import socketserver
import os

PORT = 8000

print("=" * 50)
print("🔄 Запускаем локальный сервер...")
print(f"📁 Текущая папка: {os.getcwd()}")
print(f"🌐 Сервер будет доступен по: http://localhost:{PORT}")
print("=" * 50)

# Проверяем, есть ли index.html
if not os.path.exists('index.html'):
    print("❌ ВНИМАНИЕ: Файл index.html не найден в текущей папке!")
    print("Создайте файл index.html или переименуйте свою главную страницу")
else:
    print("✅ index.html найден")

try:
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("\n🎯 Сервер успешно запущен!")
        print("📖 Открой браузер и перейди на http://localhost:8000")
        print("⏹️  Для остановки сервера нажми Ctrl+C\n")
        
        httpd.serve_forever()
        
except OSError as e:
    print(f"❌ Ошибка: Порт {PORT} уже занят!")
    print("Попробуй другой порт, например: 8080, 3000")
except KeyboardInterrupt:
    print("\n🛑 Сервер остановлен")
except Exception as e:
    print(f"❌ Неизвестная ошибка: {e}")