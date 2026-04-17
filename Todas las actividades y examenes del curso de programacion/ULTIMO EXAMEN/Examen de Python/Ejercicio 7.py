def es_primo(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lista_original = [2, 4, 7, 10, 13, 15, 19, 20]
primos = [n for n in lista_original if es_primo(n)]

print(f"Numeros primos: {primos}")