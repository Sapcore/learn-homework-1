"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def what_should_you_do(user_age):
    if user_age < 2 or user_age > 90:
        return 'You should be at home'
    elif user_age < 7:
        return 'You should be at kindergarten'
    elif user_age < 18:
        return 'You should be at school'
    elif user_age < 25:
        return 'You should be at university'
    else:
        return 'You should be at work'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    while True:
        try:
            age = float(input('How old are you? '))
        except ValueError:
            print('Please input a number')
            continue
        if age < 0 or age > 150:
            print('Input realistic age')
            continue
        break

    location = what_should_you_do(age)
    print(location)


if __name__ == "__main__":
    main()
