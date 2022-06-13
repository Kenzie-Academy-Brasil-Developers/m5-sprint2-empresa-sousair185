from datetime import datetime, date


class Funcionario:
    funcao = "Funcionario"

    def __init__(self, nome_completo: str, cpf: str, salario=3000) -> None:
        self.nome_completo = (" ").join(
            [nome.capitalize() for nome in nome_completo.split()])
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self) -> str:
        return f'<Função: {self.funcao}, Nome: {self.nome_completo}>'
