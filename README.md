# Yandex.Alice-Learning-Python-Skill
Навык Алисы для изучения программирования с использованием alice-scripts, Flask, JSON.
---------------КАК ЗАПУСТИТЬ-----------------
1)Запустить flask-приложение, т.е. это приложение(тк Skill - это класс, наследующий flask.Flask)
>>> set FLASK_APP=alice2.py    (Сохраняя пробелы)
>>> set FLASK_ENV=development
>>> flask run --with-threads
2)Запустить ngrok.exe http 5000 
3) {webhook}/post из ngrok.exe добавить в yandex.dialogs или https://station.aimylogic.com/
"""
