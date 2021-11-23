def punkt_1(surname: str, name: str) -> str:
    wynik = 'Cześć, {} {}'.format(name,surname)
    return wynik
print(punkt_1("name","namee"))


def punkt_2(i1: int, i: int) -> int:
    return i1*i

print(punkt_2(1,2))
def punkt_3(i_liczba: int) -> bool:


if(i_liczba%2):
    return True
else:
    #     return False
    return i_liczba%2 == 0

czy_mod2 = punkt_3(1)
if(czy_mod2):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
def punkt_4(arg: int, arg2: int, arg3: int) -> bool:
    return arg + arg2 >= arg3


print(punkt_4(1, 2, 3))
def punkt_5(listaa: list, int_e: int) -> bool:
    wynik = False
    for each in listaa:
        if(each==int_e):
            wynik=True
            continue;
    return wynik
s = [1,2,3]
punkt_5(s,2)

def punkt_6(l1:list,l2:list) ->list:
    #marged = l1+l2
    #lista=list(dict.fromkeys(marged))
    return list(number**3 for number in (list(set(l1+l2)))) #[]
    #return lista

print(punkt_6([1,2,3,4],[2,3,5,6]))

def punkt7():