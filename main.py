from classes.funcionario import Funcionario


def main() -> None:
    funcionario_teste = Funcionario("Igor Rodrigues de Sousa", "12312312312")
    print(f'{funcionario_teste.__dict__=}')
    print(f'{funcionario_teste}')


if __name__ == "__main__":
    main()
    # Faça os testes aqui
