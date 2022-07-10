import random
import numpy as np
from objects import Barrels, Ticket

numbers = list(range(1, 91))
random.shuffle(numbers)

print('Example: ', numbers)

barrel = Barrels()
our_numbers = barrel.show_numbers()
print(type(our_numbers))
print("Создали список: ", our_numbers)

for i in range(2):
    i = barrel.take_number()
    our_numbers = barrel.show_numbers()
    print('Вытащили бочонок: ', i)
    print('Новый список: ', our_numbers)

t = np.random.randint(1, 90, 15)
print(t)

total_indices = [(i,j) for i in range(3) for j in range(9)]
print(total_indices)

first_row = random.sample(total_indices[:9],5)
second_row = random.sample(total_indices[9:18], 5)
third_row = random.sample(total_indices[-9:], 5)

print(first_row)
print(second_row)
print(third_row)

my_ticket = Ticket()

print('Карточка: ')
print(my_ticket.show())