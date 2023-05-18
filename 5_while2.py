"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {
    'how are you?': 'Thank you, I\'m good.',
    'what are you doing?': 'I am coding.',
    'what is the weather like today?': 'It is quite sunny and warm.'

}


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    print('Print "Stop" to exit the loop.')
    while (question := input('Ask me a question: ').lower()) != 'stop':
        print(answers_dict.get(question, 'I do not have an answer. Please try another question.'))


if __name__ == "__main__":
    ask_user(questions_and_answers)
