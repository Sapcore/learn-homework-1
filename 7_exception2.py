"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

"""


def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except ValueError or TypeError:
        print('Price and discount needs to be numbers. Maximum discount needs to be an integer.')
        print('Zero price is returned.')
        return 0
    if max_discount >= 100:
        print('Max discount value is too high!')
        print('Zero price is returned.')
        return 0
    if discount >= max_discount:
        print('Actual price value is greater than maximum value allowed. Initial price value is returned.')
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
