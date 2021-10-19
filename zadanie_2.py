# Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
# wyświetli każde z nich.
# def zadanie2a(list):
#     for i in list:
#         print(i)


# names = ['Martin', 'Tom', 'Eva', 'Marcin', 'Mateusz']
# zadanie2a(names)
# Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
# liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie
# należy wykonać w 2 wersjach:
#
# def zadanie2b_1(liczby):
#     list_result = []
#     for i in liczby:
#         list_result.append(2 * i)
#     return list_result
#
# list_numbers = [2, 3, 4, 5, 6]
# print(zadanie2b(list_numbers))
#
# def zadanie2b_2(liczby):
#     list_results = [2*i for i in liczby]
#     return list_results
#
# list_numbers2 = [12, 3, 4, 5, 6]
# print(zadanie2b_2(list_numbers2))

# def zadanie2c(lista):
#     for i in range(10):
#         if lista[i] % 2 == 0:
#             print(lista[i])
#
#
# list_numbers10 = [12, 3, 4, 5, 6,2, 3, 4, 5, 12]
# zadanie2c(list_numbers10)

def zadanie2d(lista):
    for i in range(10):
        if i % 2 == 0:
            print(lista[i])


list_numbers10 = [12, 3, 4, 5, 6,2, 3, 4, 5, 12]
zadanie2d(list_numbers10)
