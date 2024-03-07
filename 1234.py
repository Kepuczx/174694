#try:
#    a = int(input())
#    b = int(input())
#    result = a/b
#
#except ZeroDivisionError:
#    print("Error")
#except ValueError:
#    print("Brak liczby")
import math


#s1 = {1:2, 2:3, 3:4}
#s2 = {v: k for k,v in s1.items()}
#print(s2)

#def rownanie_kwadratowe(a, b, c):
#    delta = b**2-4*a*c
#    if delta < 0:
#        print('brak pierwiastkow')
#        return 0
#    elif delta == 0:
#        x = -b/(2*a)
#        print('jeden pierwiastek')
#        return x
#    elif delta > 0:
#        x1 = (-b + math.sqrt(delta)) / (2*a)
#        x2 = (-b - math.sqrt(delta)) / (2 * a)
#        print('dwa pierwiastki')
#        return x1, x2
#
#
#print(rownanie_kwadratowe(6, 1, 3))
#print(rownanie_kwadratowe(1, 2, 1))
#print(rownanie_kwadratowe(1, 4, 1))


#def dlugosc_odcinka(x1=1 , x2=2, y1=3, y2=4):
#    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#print(dlugosc_odcinka())
#print(dlugosc_odcinka(2,4,5,7))
#print(dlugosc_odcinka(x1=1,x2=5,y1=6,y2=7))
#
#plik = open('text.txt','a+',encoding='utf-8')
##plik.seek(0)
##znaki = plik.read(10)
#plik.write('aaaadg')
#plik.close()
##print(znaki)


with open('text.txt', 'r') as plik:
    znaki = plik.readlines()

print(znaki)