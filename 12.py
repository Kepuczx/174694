import random
#zad 1
#A = [1-x for x in range(1,10)]
#B = [4**x for x in range(8)]
#C = [x for x in B if x % 2 == 0]
#
#print(A)
#print(B)
#print(C)

#zad2

#lista1 = []
#
#for i in range(9):
#    lista1.append(random.randint(0,100))
#
#new_list = [x for x in lista1 if x % 2 ==0]
#
#print(lista1)
#print(new_list)

#zad3

produkty = {"kg":"banan", "l":"mleko", "sztuki":"arbuz"}

sztuki = [value:key in produkty.items() if value == sztuki]
print(sztuki)