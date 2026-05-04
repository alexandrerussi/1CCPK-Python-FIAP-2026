lista_frutas = ["Abacaxi", "Banana", "Kiwi"]

# lista_frutas[0] = "Abacaxi"
# lista_frutas[1] = "Banana"
# lista_frutas[2] = "Kiwi"
print(lista_frutas[0])

lista_frutas.append("Uva")
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)