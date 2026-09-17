texto = "Teste de uso: aaasdiadaw7dyaaw"
letra_para_contar = "a"
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador += 1
print(f"A letra aparece {contador} vezes")