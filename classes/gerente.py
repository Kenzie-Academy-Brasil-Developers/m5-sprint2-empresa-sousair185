from classes.funcionario import Funcionario


class Gerente(Funcionario):
    funcao = "Gerente"

    def __init__(self, nome_completo: str, cpf: str, salario=8000) -> None:
        super().__init__(nome_completo, cpf, salario)
        self.funcionarios = []

    def __len__(self):
        return len(self.funcionarios)

    def adicionar_funcionario(self, funcionario: str) -> None:
        dict_funcionario = funcionario.__dict__
        if (
            funcionario.funcao == "Gerente" or
            funcionario.empresa != self.empresa
        ):
            return False
        for nome in self.funcionarios:
            if nome["cpf"] == dict_funcionario["cpf"]:
                return False
        self.funcionarios.append(dict_funcionario)
        return True

    def aumento_salarial(self, funcionario: str, empresa: str) -> None:
        for funcionario_do_gerente in self.funcionarios:
            if funcionario.cpf == funcionario_do_gerente['cpf']:
                funcionario.salario = round(funcionario.salario * 1.1)
                if funcionario.salario > 8000:
                    funcionario = Gerente(
                        funcionario.nome_completo,
                        funcionario.cpf,
                        funcionario.salario
                    )
                return funcionario
        return False
