a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triangulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triangulo Isósceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Não é possível formar um triângulo")
