import datetime

def obter_ano_de_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922 a 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo permitido.")
        except ValueError:
            print("Ano de nascimento inválido. Digite um valor numérico válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento
    return idade

nome_completo = input("Digite o nome completo: ")
ano_nascimento = obter_ano_de_nascimento()

idade = calcular_idade(ano_nascimento)

print(f"Nome: {nome_completo}")
print(f"Idade em 2023: {idade} anos")
