import json

# Dicionário em Python
dados = {"nome": "Maria", "idade": 30, "ativo": True}

# Convertendo para string JSON
json_str = json.dumps(dados, indent=4, ensure_ascii=False)

print(json_str)
