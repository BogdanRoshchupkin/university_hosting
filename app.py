from flask import Flask, send_from_directory

# Указываем, что статика находится в корневой папке (текущей директории)
app = Flask(__name__, static_url_path='', static_folder='.')


@app.route('/')
def home():
    # Открываем и возвращаем содержимое index.html
    with open('index.html', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    app.run(debug=True)
