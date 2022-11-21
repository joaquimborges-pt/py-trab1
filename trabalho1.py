#DMAM - 23019: Programacao
# Trabalho 1
# realizado por Joaquim Borges (1200523)
def main() -> None:
    menu()

def menu() -> None:
    dict_fun = {1: pitagoras, 2 : resolvente, 3 : mersenne, 4:harmonico}
    print("MENU")
    print("1 - Teorema de Pitágoras")
    print("2 - Fórmula Resolvente")
    print("3 - Primo de Mersenne")
    print("4 - Número Harmónico")
    opcao = int(input("Insira a opção desejada:\n"))
    dict_fun[opcao]()


def pitagoras() -> None:
    print("Teorema de Pitágoras")

def resolvente() -> None:
    print("Fórmula Resolvente")


def mersenne() -> None:
    print("Primo de Mersenne")


def harmonico() -> None:
    print("Número Harmónico")



if __name__ == "__main__":
    main()