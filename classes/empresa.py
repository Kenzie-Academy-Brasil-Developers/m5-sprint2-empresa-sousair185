from calendar import month
from datetime import datetime
import json
import os

from classes.gerente import Gerente


class Empresa:
    def __init__(self, nome: str, cnpj: int) -> None:
        self.nome = " ".join([nome.capitalize() for nome in nome.split()])
        self.cnpj = cnpj
        self.contratados = []

    def __len__(self) -> None:
        return len(self.contratados)

    def contratar_funcionario(self, funcionario: str) -> None:
        lower_name = "_".join(funcionario.nome_completo.split()).lower()
        lower_empresa = "".join(self.nome.split()).lower()
        email = f'{lower_name}@{lower_empresa}.com'
        funcionario_contratado = funcionario.__dict__

        for contratado in self.contratados:
            if contratado["cpf"] == funcionario_contratado["cpf"]:
                return "CPF já consta como contratado!"

        funcionario_contratado["email"] = email
        funcionario_contratado["empresa"] = self.nome
        return "Funcionário Contratado!"

    def gerar_holerite(self, funcionario: str) -> None:
        empresa = "_".join(self.nome.split()).lower()
        nome = "_".join(funcionario.nome_completo.split()).lower()

        for contratado in self.contratados:
            if funcionario.__dict__["cpf"] == contratado["cpf"]:
                path = f'./empresas/{empresa}/{nome}.json'
                os.system(f'mkdir ./empresas/{empresa}')
                date = datetime.now()
                month = {"mês": date.strftime("%B")}
                with open(path, "w") as file:
                    data = {**funcionario.__dict__, **month}
                    data.pop('email', None)
                    data.pop('empresa', None)
                    json.dump(data, file, indent=4)
                    return True
        return False

    def demitir_funcionario_gerente(self, funcionario: str) -> None:
        func_dict = funcionario.__dict__
        for contratado in self.contratados:
            if 'funcionarios' in contratado:
                contratado['funcionarios'] = [
                    f for f
                    in contratado['funcionarios']
                    if f["cpf"] != func_dict["cpf"]
                ]

    def verificar_se_esta_contratado(self, funcionario: str) -> None:
        func_dict = funcionario.__dict__
        for contratado in self.contratados:
            if contratado["cpf"] == func_dict["cpf"]:
                return True
        return False

    def demissao(self, funcionario):
        self.demitir_funcionario_gerente(funcionario)
        func_dict = funcionario.__dict__
        for contratado in self.contratados:
            if contratado["cpf"] == func_dict["cpf"]:
                self.contratados = [
                    c for c in self.contratados if c["cpf"] != func_dict["cpf"]
                ]

                if funcionario.funcao == "Gerente":
                    return "Gerente demitido!"
                return "Funcionário demitido!"
        return "Não consta esse CPF na empresa"

    @classmethod
    def ler_holerite(cls, empresa: str, funcionario: str) -> None:
        try:
            empresa_path = "_".join(empresa.nome.split()).lower()
            funcionario_file = "_".join(
                funcionario.nome_completo.split()
            ).lower()
            path = f"./empresas/{empresa_path}/{funcionario_file}.json"
            with open(path, "r") as file:
                holerite = json.load(file)
                return holerite
        except Exception:
            return "Holerite ainda não foi gerado"

    def promocao(self, funcionario: str) -> None:
        for contratado in self.contratados:
            if contratado['cpf'] == funcionario.cpf:
                nome = funcionario.nome_completo
                cpf = funcionario.cpf
                novoGerente = Gerente(nome, cpf)
                self.demissao(funcionario)
                funcionario = novoGerente
                self.contratar_funcionario(funcionario)
                return novoGerente
        return False
