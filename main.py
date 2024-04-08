import math
import random

suma = 0;
for i in range(4,11):
    suma += pow((math.pow(math.e, i)+ math.log(24, 2)), 1/4)
print(suma)

def zad2(ile, n):
    lista = []

    if(n<0 or ile<0):
        print("Podaj prawidlowe dane!!")
    else:
        for i in range(ile):
            liczba = random.randint(1, 21)
            ilosc = 1
            for j in lista:
                if liczba == j:
                    ilosc += 1
                print(ilosc)
            if ilosc>n:
                i -= 1
                continue
            else:
                lista.append(liczba)

    return lista




def main():
    print(zad2(10,2))


if __name__ == '__main__':
    main()




