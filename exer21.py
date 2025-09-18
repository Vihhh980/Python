print('Primeiro ponto')
x1 = float(input('Digite o primeiro número (X1)'))
y1 = float(input('Digite o primeiro número (Y1)'))
print('Segundo ponto')
x2 = float(input('Digite o primeiro número (X2)'))
y2 = float(input('Digite o primeiro número (Y2)'))

subtracaox = x1 - x2
subtracaoy = y1 - y2
quadrado = (subtracaox ** 2)
quadrado2 = (subtracaoy ** 2)
soma = quadrado - quadrado2
resultado= soma ** 0.05

print('A distância entre dois pontos é', resultado)
