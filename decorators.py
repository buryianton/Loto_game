#Функция декоратора

def add_separators(f):
    #inner - итоговая функция с новым поведением
    def inner(*args):
        #поведение до вызова
        print('-'*26)
        result = f(*args)

        #поведение после вызова
        print('-'*26)
        return result


    #возвращаем функцию с inner поведением
    return inner