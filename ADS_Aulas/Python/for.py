#PRIMEIRO USO
texto = "Teste de uso: aaasdiadaw7dyaaw"
letra_para_contar = "a"
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador += 1
print(f"A letra aparece {contador} vezes")

#LISTA COM FOR
numeros = [1, 2, 3, 4, 5, 5]
soma = 0

for numero in numeros:
    soma += numero
print(soma)