a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))   
c = int(input("Terceiro valor: "))  
# Verificando que é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando que é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
