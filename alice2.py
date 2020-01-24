from alice_scripts import Skill, request, say, suggest
import pymorphy2
import random

# ПРИГОТОВЛЕНИЯ

skill = Skill(__name__)
morph = pymorphy2.MorphAnalyzer()

help_buttons = (
    'Научи',
    'Давай тест',
    'Факт',
)
wrong_ans = (
    'Как жаль, что я не знаю таких слов, лучше нажми на кнопки',
    'Тссссс, тихо, нельзя такое произносить в здесь, лучше нажми на кнопку',
    'Cейчас нужно учиться, а для этого надо нажать на кнопку',

)
chapters = (
    'Ввод и вывод данных',
    'Вычисления',
    'Условия',
    'Циклы',
    'Строки',
    'Массивы',
    'Множества',
    'Словари',
    'Функции'
)
questions = {   #*Дописать вопросы
    "questions": [
        {
            "question": "Как вывести 'Hello world!'",
            "variants": [
                "print('Hello world!')",
                "write('Hello world!')"
            ],
            "answer": "print('Hello world!')"
        },
        {
            "question": "Как вывести 'First!'",
            "variants": [
                "print('First!')",
                "write('Second!')"
            ],
            "answer": "print('First!')"
        }
    ]
}
facts = {   #*Дописать факты
    "facts": [
        {
            "code": ">>>max_xy = lambda x,y: x if x > y else y\n",
            "description": "Это очень интересная вещь в Python - Лямбда функция!\nПопробуй запустить эту программу!"
        },
        {
            "code": "4*sum((-1.0)**(n%2) / (2*n + 1) for n in range(2010))\n",
            "description": "Вычисление числа Пи в одну строчку!\nЗапусти эту программу!"
        },
        {
            "code": "max_xy = lambda x,y: x if x > y else y\n",
            "description": "Это одна из реализаций лямбда функций.\nОчень интересный интрумент в Python!",
        }
    ]
}
facts = facts['facts']


# -------------------------------------------------------------
# ОСНОВНОЙ БЛОК ПРОГРАММЫ (ВЕТВЛЕНИЕ)


@skill.script
def run_script():
    yield say('Ну здравствуй, ученик, что хочешь узнать о Python?'
              'Выбери команды ниже, я не кусаюсь!',
              suggest(*help_buttons),
              )
    while True:
        if request.has_lemmas('учить', 'научить', 'обучи'):
            yield say("Выберите главу", suggest(*chapters))
            chapter = yield from plan()
            if not chapter:
                yield say('Хорошо, выбирай опцию!',
                          suggest(*help_buttons))
        elif request.has_lemmas('факт'):
            ej = True
            while ej:
                num = random.randint(0, 2)
                yield say(facts[num]['code'] + facts[num]['description'],
                          suggest('Ещё!', 'Хватит'))
                if request.command == 'Ещё!':
                    ej = True
                elif request.command == 'Хватит':
                    ej = False
            yield say('Жаль, что вы вышли, а можно было бы ещё посмотреть!\n'
                      'Тыкай на кнопку',
                      suggest(*help_buttons)
                      )
        elif request.has_lemmas('помощь', 'помогать'):
            pass
        elif request.has_lemmas('тест'):
            req = yield from test()
            if req >= 0:
                q = morph.parse('вопрос')[0]
                q = q.make_agree_with_number(req).word
                yield say('Вы ответили правильно на {0} {1}!\n'.format(req, q) +
                          'Так держать!\n' + 'Выберите команды',
                          suggest(*help_buttons)
                          )
            elif req == -1:
                yield say('Жаль, что вы вышли, а можно было бы ещё подумать!\n'
                          'Тыкай на кнопку',
                          suggest(*help_buttons)
                          )
        else:
            yield say(*wrong_ans, suggest(*help_buttons))


# ------------------------------------------------------------------------------


def plan():     #*Дописать теорию.
    ans = request.command
    if ans.lower() == 'назад':
        return False
    elif ans.lower() == 'ввод и вывод данных':
        pass
    elif ans.lower() == 'вычисление':
        pass
    elif ans.lower() == 'условия':
        pass
    elif ans.lower() == 'циклы':
        pass
    elif ans.lower() == 'строки':
        pass
    elif ans.lower() == 'массивы':
        pass
    elif ans.lower() == 'множества':
        pass
    elif ans.lower() == 'словари':
        pass
    elif ans.lower() == 'функции':
        pass


# ------------------------------------------------------------------------------
# РЕАЛИЗАЦИЯ ТЕСТА, в questions.json - вопросы


def test():
    global count
    count = 0
    first = True
    for quest in questions['questions']:
        if first:
            yield say('Хорошо, давай начнём!\n' + quest['question'],
                      suggest(*quest['variants'], 'Завершить тест')
                      )
            first = False
        else:
            yield say('Следующий вопрос!\n' + quest['question'],
                      suggest(*quest['variants'], 'Завершить тест')
                      )
        if request.command == quest['answer']:
            count += 1
        elif request.command == 'завершить тест':
            return -1
    return count


# ------------------------------------------------------


"""
---------------КАК ЗАПУСТИТЬ-----------------
1)Запустить flask-приложение, т.е. это приложение(тк Skill - это класс, наследующий flask.Flask)
>>> set FLASK_APP=alice2.py    (Сохраняя пробелы)
>>> set FLASK_ENV=development
>>> flask run --with-threads
2)Запустить ngrok.exe http 5000 
3) {webhook}/post из ngrok.exe добавить в yandex.dialogs или https://station.aimylogic.com/
"""
