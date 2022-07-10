import random
import numpy as np

class Barrels:

    def __init__(self):
        self.numbers = list(range(1, 91))
        random.shuffle(self.numbers)

    def show_numbers(self):
        return self.numbers

    def take_number(self):
        barrel = self.numbers[0]
        del self.numbers[0]
        return barrel


class Ticket:

    def __init__(self):
        self.ticket_array = np.zeros((3,9), dtype=int)
        total_indices = [(i,j) for i in range(3) for j in range(9)]
        random_indices = []

        #берем случайным образом индексы, которые будем заполнять значениями
        first_row = random.sample(total_indices[:9],5)
        second_row = random.sample(total_indices[9:18], 5)
        third_row = random.sample(total_indices[-9:], 5)

        for i in first_row:
            random_indices.append(i)

        for i in second_row:
            random_indices.append(i)

        for i in third_row:
            random_indices.append(i)

        #заполняем индексы карточки случайными значениями
        numbers = np.random.randint(1, 90, 15)
        for num in random_indices:
            self.ticket_array[num] = numbers[0]
            numbers = numbers[1:]

    def show(self):
        return self.ticket_array



