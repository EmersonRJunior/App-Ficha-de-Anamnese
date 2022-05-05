class Ficha_anamnese:
    def __init__(self):
        self.dados = {}
        pass

    def dados_pessoais(self):
        dados = {
            "Nome": input("Nome completo do paciente:\n"),
            "Idade": input("Idade do paciente:\n"),
            "CPF": input("CPF do paciente:\n")
        }
        self.dados["Dados Pessoais"] = dados

    def habitos_diários(self):
        dados = {
            "Tratamento estético anterior": input("O paciente ja passou por outro procedimento estético? (Sim/Nao)\n"),
            "Medicamentos": input("O paciente usa algum medicamento? (Sim/Nao)\n"),
            "Quais Medicamentos": "",

        }
        if dados["Medicamentos"] == "Sim":
            dados["Quais Medicamentos"] = input(
                "Quais os medicamentos em uso? \n")
        self.dados["Habitos Diários"] = dados

    def historico_clinico(self):
        pass

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
    print(ficha.dados)
    ficha.dados_pessoais()
    ficha.habitos_diários()
    print(ficha.dados)
    salvar.salvar()
