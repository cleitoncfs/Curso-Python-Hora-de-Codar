from datetime import datetime


def obter_ano_nascimento(ano_atual):
    while True:
        try:
            ano = int(input("Em que ano você nasceu? "))
            if 1900 <= ano <= ano_atual:
                return ano
            print(f"Por favor, digite um ano válido entre 1900 e {ano_atual}.")
        except ValueError:
            print("Entrada inválida! Digite apenas números (ex: 1995).")


def calcular_idade():
    print("=" * 35)
    print("      CALCULADORA DE IDADE")
    print("=" * 35)

    ano_atual = datetime.now().year
    ano_nascimento = obter_ano_nascimento(ano_atual)
    idade = ano_atual - ano_nascimento

    print("-" * 35)
    print(f"Você tem (ou vai fazer) {idade} anos em {ano_atual}.")
    print("=" * 35)


if __name__ == "__main__":
    calcular_idade()
