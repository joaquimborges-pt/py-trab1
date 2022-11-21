#DMAM - 23019: Programacao
# Trabalho 1
# realizado por Joaquim Borges (1200523)
def main() -> None:
    menu()

def menu() -> None:
    print("MENU")
    print("1 - Teorema de Pitágoras")
    print("2 - Fórmula Resolvente")
    print("3 - Primo de Mersenne")
    print("4 - Número Harmónico")
    opcao = int(input("Insira a opção desejada:\n"))
    test_dict = {1: "pitagoraica", 2 : "resolvent", 3 : "mersenne", 4:"hramonico"}
    print(test_dict[1])
    #print("opcao:", opcao)








if __name__ == "__main__":
    main()