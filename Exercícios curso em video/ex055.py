maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'digite {c}°: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O menor peso é {menor}')
print(f'O maior peso é {maior}')
