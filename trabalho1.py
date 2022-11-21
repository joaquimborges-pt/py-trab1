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
    dict_fun[opcao: int]()


def pitagoras() -> None:
    from math import sqrt
    print("Teorema de Pitágoras")
    catet1 = int(input("Introduza o comprimento do primeiro cateto:\n"))
    catet2 = int(input("Intoduza o comprimento do segundo cateto:\n"))
    hipotenusa = sqrt(catet1**2 + catet2**2)
    print(f'A hipotenusa do triângulo com catetos {catet1} e {catet2} é igual a ', hipotenusa)

def resolvente() -> None:
    from math import sqrt
    print("Fórmula Resolvente")
    a = int(input("Introduza o valor de a:\n"))
    b = int(input("Intoduza o valor de b:\n"))
    c = int(input("Introduza o valor de c:\n"))
    factor = b**2 - 4*a*c
    if factor >= 0:
        x1 = sqrt(factor) - b
        x2 = -1*(sqrt(factor) + b)
        print(f'As raizes da equação com a={a}, b={b} e c={c} são: x1={x1} e x2={x2}')
    else:
        print("Não existem soluções reais.")

def mersenne() -> None:
    from math import sqrt
    print("Primo de Mersenne")
    num = int(input("Introduza um numero de n:\n"))


def harmonico() -> None:
    from math import sqrt
    print("Número Harmónico")
    num = int(input("Introduza um numero de n:\n"))



if __name__ == "__main__":
    main()
