import sys

def zad1():
    zdanie = input("Napisz zdanie panie kolego: ")

    lista = zdanie.split()


    print(len(lista),lista)

def zad2():
    lista = []
    for i in range(1, 4, 1):
        a = int(input("Podaj liczbe: "))
        lista.append(a)
    result = lista[0]**lista[1]+lista[2]
    print(result)

    #sys.stdout.write("Podaj liczbe: ")
    #b = sys.stdin.readline()
    #print(b)
    #print(type(b))

def zad3():
    napis = input("Podaj wyraz: ")
    lista1 = []
    for i in napis:
        lista1.append(i)
    lista2 = lista1[::-1]

    if lista1 == lista2:
        print("JEST TO PALINDROM")
    else:
        print("NIE JEST TO PRALINDROM")

def zad4():
    liczba = int(input("Podaj liczbe: "))
    if liczba == 2 or liczba == 3:
         print("Jest to liczba pierwsza")
    elif liczba%3 == 0 or liczba%2 == 0:
        print("Nie jest to liczba pierwsza")
    else:
        print("Jest to liczba pierwsza")

def zad5():
    liczby = []
    doskonala = []
    for i in range(1,1001):
        liczby.append(i)

    for j in range(len(liczby)):
        a = liczby[j]
        dzielniki = []
        for h in range(1,a):
            if a % liczby[h] == 0:
                dzielniki.append(liczby[h])
        if liczby[j] == sum(dzielniki):
            doskonala.append(a)
    print(doskonala)



def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    zad5()
if __name__ == '__main__':
    main()