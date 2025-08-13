def main():
    print_square(3)


def print_square(n):
    # PARA CADA COLUNA
    for i in range(n):

        # PARA CADA TIJOLO
        for j in range(n):

            # PRINT TIJOLO
            print('#', end='')

        # CRIAR LINHA VAZIA ABAIXO
        print()


main()

"""
# OUTRA FORMA DE IMPRESSAO NA TELA 
def print_square(n):
    for i in range(n):
        print('#' * n)
"""