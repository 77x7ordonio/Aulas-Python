#Desenvolva um programa utilizando o para que faça a tabuada de um número
#inteiro que será digitado pelo usuário. Mas a tabuada não deve necessariamente
#iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados pelo
#usuário

numero = int(input("***Tabuada Easy 2.0***\nMontar a tabuada do: "))

comeco = int(input("Calcular de: "))
fim = int(input("Calcular até: "))

for i in range(comeco, fim + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
