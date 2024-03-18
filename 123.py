import random

def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    #zad6()
    #zad7()
    #zad8()
    #zad9()
    #zad10()
    #zad11()
    #zad12()
    zad13()

def zad1():
    zdanie = input("Podaj zdanie")
    x = zdanie.split()
    z = len(x)

    print(z)


def zad2():
    a = int(input())
    b = int(input())
    c = int(input())

    wynik = a**b+c

    print(wynik)

def zad3():
    napis = input("Sprawdz czy wyraz jest palindromem: ")
    table = []

    for x in range(0, len(napis)):
        table.append(napis[x])

    if table == table[::-1]:
        print("Wyraz ten jest palindromem.")
    else:
        print("Nie jest")


def zad4():

    liczba = int(input("Sprawdz czy liczba jest pierwsza: "))

    if liczba == 2 or liczba == 3:
        print("Liczba jest pierwsza")
    elif liczba % 2 == 0 or liczba % 3 == 0 or liczba == 1:
        print("Liczbe nie jest liczba pierwsza")
    else: print("Liczba jest pierwsza")


def doskonale_liczby(number):

    tabela = []

    for i in range(1, number):
        if number % i == 0:
            tabela.append(i)

    suma = 0

    for i in tabela:
        suma += i
    if suma == number:
        return True

def zad5():
    liczby = []
    doskonale = []

    for i in range(1, 10000): liczby.append(i)

    for i in liczby:
        if doskonale_liczby(i) == True:
            doskonale.append(i)

    print(doskonale)


def zad6():
    lista = []

    for i in range(1,100,2):
        lista.append(int(i))
        lista.append(float(i+1))

    for i in range(len(lista)):
        lista[i] = i**2

    print(lista)

def zad7():
    i = 0
    tabela = []

    while i < 10:
        i += 1
        x = int(input())
        if x % 2 == 0:
            tabela.append(i)

    print(tabela)

def zad8():
    lista = [1,"siea","t532a",24,15,11,1,15,"siea",15]
    slownik = {}

    for i in lista:
        if i in slownik:
            slownik[i] += 1
        else:
            slownik[i] = 1

    keytodelete = [key for key in slownik if not isinstance(key,(int,float))]

    for key in keytodelete:
        del slownik[key]


    print(slownik)


def zad9():
    A = [x-1 for x in range(1,11)]
    B = [4**x for x in range(8)]
    C = [x for x in B if x % 2 == 0]

    print(A)
    print(B)
    print(C)

def zad10():
    lista1 = []

    for i in range(10):
        lista1.append(random.randint(1,11))

    lista2 = [x for x in lista1 if x % 2 == 0]

    print(lista1)
    print(lista2)

def zad11():
    slownik = {"banan":"kg","paluszki rybne":"sztuki","jablka":"kg"}

    sztuki = [key for key in slownik if slownik[key] == "sztuki"]


    print(slownik)
    print(sztuki)

def zad12():
    trojkat = []

    for i in range(3):
        trojkat.append(int(input()))

    trojkat.sort()

    if (trojkat[0]**2) + (trojkat[1]**2) == (trojkat[2]**2):
        print("Trojkat jest prostokatny")
    else:
        print("Trojkat nie jest prostokatny")

def zad13():

    


if __name__ == '__main__':
    main()