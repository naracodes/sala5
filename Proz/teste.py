import datetime

while True:
    nome = input("Digite seu nome completo: ")
    ano = input("Digite seu ano de nascimento (entre 1923 e 2022): ")
    try:
        ano = int(ano)
        if ano < 1923 or ano > 2022:
            print("Ano inválido. Tente novamente.")
            continue
        idade = datetime.date.today().year - ano
        print(f"Olá, {nome}! Você completou ou completará {idade} anos em 2023.")
        break
    except ValueError:
        print("Valor inválido. Tente novamente.")