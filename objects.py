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

        for col in range(9):
            if (self.ticket_array[0][col] != 0 and self.ticket_array[1][col] != 0 and self.ticket_array[2][col] != 0):
                for row in range(2):
                    if self.ticket_array[row][col] > self.ticket_array[row+1][col]:
                        temp = self.ticket_array[row][col]
                        self.ticket_array[row][col] = self.ticket_array[row+1][col]
                        self.ticket_array[row+1][col] = temp

                    elif (self.ticket_array[0][col] != 0 and self.ticket_array[1][col] != 0 and self.ticket_array[2][col] == 0):
                        if self.ticket_array[0][col] > self.ticket_array[1][col]:
                            temp = self.ticket_array[0][col]
                            self.ticket_array[0][col] = self.ticket_array[1][col]
                            self.ticket_array[1][col] = temp

                    elif (self.ticket_array[0][col] != 0 and self.ticket_array[2][col] != 0 and self.ticket_array[1][col] == 0):
                        if self.ticket_array[0][col] > self.ticket_array[2][col]:
                            temp = self.ticket_array[0][col]
                            self.ticket_array[0][col] = self.ticket_array[2][col]
                            self.ticket_array[2][col] = temp

                    elif (self.ticket_array[0][col] == 0 and self.ticket_array[1][col] != 0 and self.ticket_array[2][col] != 0):
                        if self.ticket_array[1][col] > self.ticket_array[2][col]:
                            temp = self.ticket_array[1][col]
                            self.ticket_array[1][col] = self.ticket_array[2][col]
                            self.ticket_array[2][col] = temp

    def show(self):
        return self.ticket_array

    def play(self, number):
        numbers = []
        for col in range(9):
            for row in range(2):
                if number == self.ticket_array[row][col]:
                    print('В карточке есть число - ', number)
                    self.ticket_array[row][col] = 0
                    numbers.append(number)

        print(self.ticket_array)
        return numbers