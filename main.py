import random
import numpy as np
from objects import Barrels, Ticket



#создаем мешок с бочонками
barrel = Barrels()
our_numbers = barrel.show_numbers()

my_ticket = Ticket()
opponent_ticket = Ticket()

print('Моя карточка: ')
print(my_ticket.show(),'\n')
print('Карточка опонента: ')
print(opponent_ticket.show(),'\n')


def play_round(number):
    num = number
    print('Вытащили бочонок c номером ', num)

    print('Ваша карточка: ')
    print(my_ticket.show(), '\n')

    answer = input('Зачеркнуть это число на вашей карточке? \n'
                   'Введите 1 или 2 \n'
                   '1. Зачеркнуть \n'
                   '2. Не зачеркивать \n')
    if answer == 1:
        if number in my_ticket:
            print('Есть')
    elif answer == 2:
        pass


my_numbers = []
opponent_numbers = []

for i in range(2):
    number = barrel.take_number()
    print('Наш бочонок с номером - ', number)
    print('МОЯ КАРТОЧКА: ')
    #my_ticket.play(number)
    play_round(number)
    print('КАРТОЧКА ОПОНЕНТА:')
    opponent_ticket.play(number)


print(my_numbers)

#print('Мои числа, вычеркнутые из карточки: ', my_numbers)
#print('Числа, вычеркнутые из карточки опонента: ', opponent_numbers)



