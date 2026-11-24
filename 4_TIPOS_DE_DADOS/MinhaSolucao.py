# Exercício 1:
# Enunciado: Crie um programa que receba dois números inteiros e exiba a soma, subtração,
# multiplicação e divisão inteira entre eles.
# Descrição: O programa deve usar operações aritméticas básicas entre dois números inteiros,
# como soma, subtração, multiplicação e divisão inteira. Os resultados devem ser exibidos
# separadamente com mensagens explicativas.

import math
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao_inteira = num1 // num2

print(f"A soma entre {num1} e {num2} é: {soma}")
print(f"A subtração entre {num1} e {num2} é: {subtracao}")
print(f"A multiplicação entre {num1} e {num2} é: {multiplicacao}")
print(f"A divisão inteira entre {num1} e {num2} é: {divisao_inteira}")

# Exercício 2:
# Enunciado: Escreva um programa que receba um número de ponto flutuante, arredonde-o para duas
# casas decimais e exiba o resultado.
# Descrição: O programa deve solicitar um número float, usar a função round() para arredondá-lo
# para duas casas decimais e exibir o valor arredondado. O programa também deve informar o número
# original.

num3 = float(input("Digite um número de ponto flutuante: "))
num3_arredondado = round(num3, 2)

print(f"O número original é: {num3}")
print(f"O número arredondado para duas casas decimais é: {num3_arredondado}")


# Exercício 3:
# Enunciado: Desenvolva um programa que converta um número inteiro em float e vice-versa,
# exibindo o resultado das conversões.
# Descrição: O programa deve receber um número inteiro e convertê-lo em float, bem como receber
# um número float e convertê-lo em inteiro. Ambos os resultados das conversões devem ser exibidos.

num4 = int(input("Digite um número inteiro: "))
num4_float = float(num4)

num5 = float(input("Digite um número de ponto flutuante: "))
num5_inteiro = int(num5)

print(f"O número inteiro convertido para float é: {num4_float}")
print(f"O número de ponto flutuante convertido para inteiro é: {num5_inteiro}")


# Exercício 4:
# Enunciado: Crie um programa que solicite três números ao usuário, aplique a fórmula de
# Bhaskara para calcular as raízes e exiba os resultados.
# Descrição: O programa deve solicitar os coeficientes `a`, `b` e `c` da equação quadrática.
# Usar o módulo math para calcular a raiz quadrada na fórmula de Bhaskara e exibir as raízes,
# se existirem. Deve incluir validação para o caso de raízes inexistentes.

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raízes reais.")
else:
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)
    print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")

# Exercício 5:
# Enunciado: Escreva um programa que use o módulo `math` para calcular a área de um círculo,
# solicitando o raio ao usuário.
# Descrição: O programa deve solicitar o raio como entrada, usar a fórmula da área de um
# círculo (A = πr²), com o módulo math para calcular π, e exibir o resultado com duas casas
# decimais.

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio**2

print(f"A área do círculo com raio {raio} é: {area:.2f}")
