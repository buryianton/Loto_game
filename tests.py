import numpy as np

def test_ticket_can_be_90():
    #numbers = np.random.randint(1, 91, 15)
    list = []
    a = 0
    t = 100
    for i in range(t):
        numbers = np.random.randint(1, 91, 15)
        count = 0
        for i in range(15):
            a = numbers[i]
            print('Число равно ', a)
            if a != 90:
                pass
            if a == 90:
                count += 1
            list.append(a)
    if 90 in list:
        print('В списке есть', count, ' чисел 90')
    if 90 not in list:
        print('После ', t, ' раз создания случайного списка в списке нет 90')

test_ticket_can_be_90()