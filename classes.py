class Ficha_anamnese:
    def __init__(self):
        self.dados = {}
        # input("\n")

    def dados_pessoais(self):
        dados = {
            "Nome": input("Nome completo do paciente:\n"),
            "Idade": input("Idade do paciente:\n"),
            "CPF": input("CPF do paciente:\n"),
            "Estado": input("Qual UF do paciente?\n"),
            "Cidade": input("Digite a cidade que o paciente mora:\n"),
            "Rua": input("Digite o nome da rua:\n"),
            "CEP": input("Digite o CEP (se souber):\n"),
            "Bairro": input("Digite o bairro:\n"),
            "Telefone": input("Telefone para contato:\n"),
            "Outro Telefone": input("O paciente possui outro telefone de contato?\n"),
            "Data Nascimento": input("Qual a data de nascimento do paciente?\n"),
            "Profissão": input("Digite a profissão do paciente:\n"),
            "Estado Civil": input("Qual o estado civil do paciente?\n"),
            "Email": input("Digite um email para contato:\n"),
        }
        if dados["Outro Telefone"] == "Sim":
            dados["Outro Telefone"] = input("Digite o Outro número: \n")
        else:
            dados["Outro Telefone"] = "Não possui outro telefone"
        self.dados["Dados Pessoais"] = dados

    def habitos_diários(self):
        dados = {
            "Tratamento estético anterior": input("O paciente ja passou por outro procedimento estético? (Sim/Nao)\n"),

        }
        self.dados["Habitos Diários"] = dados

    def historico_clinico(self):
        dados = {
            "Tratamento Médico Atual": "",
            "Medicamentos": input("O paciente usa algum medicamento? (Sim/Nao)\n"),
            "Quais Medicamentos": "",

        }
        if dados["Medicamentos"] == "Sim":
            dados["Quais Medicamentos"] = input(
                "Quais os medicamentos em uso? \n")
        self.dados["Histórico Clínico"] = dados

    def termo_responsabilidade(self):
        pass


class Salvar_pdf(Ficha_anamnese):
    def __init__(self):
        super().__init__()
        dados = self.dados

    def salvar(self):
        pass


if __name__ == "__main__":
    ficha = Ficha_anamnese()
    salvar = Salvar_pdf()
    ficha.dados_pessoais()
    ficha.habitos_diários()
    print(ficha.dados)
    salvar.salvar()
