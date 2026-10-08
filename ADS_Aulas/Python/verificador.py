def calcular_digito(cpf_parcial):
	soma = 0
	peso = len(cpf_parcial) + 1

	for numero in cpf_parcial:
		soma += int(numero) * peso
		peso -= 1

	resto = soma % 11
	return "0" if resto < 2 else str(11 - resto)


def gerar_cpf(cpf_base):
	cpf_base = cpf_base.strip()
	if len(cpf_base) != 9 or not cpf_base.isdigit():
		raise ValueError("Informe exatamente os 9 primeiros dígitos do CPF.")

	primeiro_digito = calcular_digito(cpf_base)
	segundo_digito = calcular_digito(cpf_base + primeiro_digito)
	cpf = cpf_base + primeiro_digito + segundo_digito

	return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def validar_cpf(cpf):
	cpf = cpf.strip().replace(".", "").replace("-", "")

	if len(cpf) != 11 or not cpf.isdigit():
		return False

	if cpf == cpf[0] * 11:
		return False

	primeiro_digito = calcular_digito(cpf[:9])
	segundo_digito = calcular_digito(cpf[:10])

	return cpf[-2:] == primeiro_digito + segundo_digito


def main():
	while True:
		print("\n1 - Gerar CPF a partir dos 9 primeiros dígitos")
		print("2 - Verificar um CPF completo")
		print("0 - Sair")
		opcao = input("Escolha uma opção: ").strip()

		if opcao == "0":
			print("Programa encerrado.")
			break
		elif opcao == "1":
			cpf_base = input("Digite os 9 primeiros dígitos: ")
			try:
				print("CPF calculado:", gerar_cpf(cpf_base))
			except ValueError as erro:
				print(erro)
		elif opcao == "2":
			cpf = input("Digite o CPF: ")
			if validar_cpf(cpf):
				print("CPF válido.")
			else:
				print("CPF inválido.")
		else:
			print("Opção inválida.")


if __name__ == "__main__":
	main()
