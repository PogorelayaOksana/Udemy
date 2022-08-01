#Создайте класс Pizza, который принимает список ингредиентов.
#Класс поддерживает:
#атрибут order_number, который возвращает текущий номер заказа
#(подсказка: используйте статический атрибут в качестве сквозного счётчика)
#атрибут ingredients, который возвращает список, принятый в конструкторе
#функции (garden_feast, hawaiian, meat_festival) создания видов пицц,
#ингредиенты которых заранее известны (см. таблицу)
#Name            Ingredients
#hawaiian            - ham, pineapple
#meat_festival    - beef, meatball, bacon
#garden_feast    - spinach, olives, mushroom
#Примеры вызовов:
#p1 = Pizza(['bacon', 'parmesan', 'ham'])    # order 1
#p2 = Pizza.garden_feast()                  # order 2
#p1.ingredients ➞ ['bacon', 'parmesan', 'ham']
#p2.ingredients ➞ ['spinach', 'olives', 'mushroom']
#p1.order_number ➞ 1
#p2.order_number ➞ 2

class Pizza:
    order_counter = 0

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        Pizza.order_counter = Pizza.order_counter + 1
        self.order_number = Pizza.order_counter

    @staticmethod
    def garden_feast():
        return Pizza(ingredients=['spinach', 'olives', 'mushroom'])

    @staticmethod
    def hawaiian():
        return Pizza(['ham', 'pineapple'])

    @staticmethod
    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])

m=Pizza.meat_festival()
h=Pizza.hawaiian()
g=Pizza.garden_feast()
# o=Pizza.order_number
print(m.ingredients)
print(h.ingredients)
print(g.ingredients)
