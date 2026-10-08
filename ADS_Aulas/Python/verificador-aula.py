def validar_cpf(cpf: str) -> bool:
    # 1. Remover caracteres não numéricos
    cpf = ''.join(c for c in cpf if c.isdigit())

    # 2. Verificar se existem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # 3. Rejeitar sequência com todos os dígitos iguais
    if cpf == cpf[0] * 11:
        return False
    
    # 4. Calcular o 1º dígito usando pesos 10..2
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # 5. Calcular o 2º dígito usando pesos 11..2
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    # 6. Comparar os dois dígitos calculados com o CPF informado
    # 7. Se ambos coincidirem -> válido
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2


if __name__ == "__main__":
   while True:
    cpf_input = input("\nDigite o CPF (ou 'sair' para encerrar): ").strip()
    
    if cpf_input.lower() == 'sair':
        break
    
    if validar_cpf(cpf_input):
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")