# 1. Verificar se um número é par ou ímpar
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é par."
    else:
        return f"{numero} é ímpar."

# 2. Calcular o preço final com desconto
def calcular_desconto(preco):
    if preco > 100:
        desconto = preco * 0.10
    else:
        desconto = preco * 0.05
    preco_final = preco - desconto
    return f"Preço final com desconto: R$ {preco_final:.2f}"

# 3. Classificação de idade
def classificar_idade(idade):
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida"

# Testando os códigos
print(verificar_par_impar(7))  # Exemplo para número ímpar
print(calcular_desconto(120))  # Exemplo para desconto maior
print(classificar_idade(30))   # Exemplo para classificação como adulto
