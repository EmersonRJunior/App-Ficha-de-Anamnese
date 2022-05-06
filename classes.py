class Ficha_anamnese:
    def __init__(self):
        self.dados = {}
        # input("\n")

    def dados_pessoais(self):
        dados = {
            "Nome": input("\nNome completo do paciente:\n"),

            "Idade": input("\nIdade do paciente:\n"),

            "CPF": input("\nCPF do paciente:\n"),

            "Estado": input("\nQual UF do paciente?\n"),

            "Cidade": input("\nDigite a cidade que o paciente mora:\n"),

            "Rua": input("\nDigite o nome da rua:\n"),

            "CEP": input("\nDigite o CEP (se souber):\n"),

            "Bairro": input("\nDigite o bairro:\n"),

            "Telefone": input("\nTelefone para contato:\n"),

            "Data Nascimento": input("\nQual a data de nascimento do paciente?\n"),

            "Profissão": input("\nDigite a profissão do paciente:\n"),

            "Estado Civil": input("\nQual o estado civil do paciente?\n"),

            "Email": input("\nDigite um email para contato:\n"),

            "Tratamento estético anterior": input("\nO paciente ja passou por outro procedimento estético? (Sim/Nao)\n"),

            "Qual tratamento estético": input("\nQual tratamento estético ja foi feito? (Deixe em branco se não houver)\n"),

            "Lente de contato": input("\nO paciente usa lente de contato?\n"),

            "Cosméticos": input("\nUsa algum cosmético? (pomadas, creme, maquiagem etc)\n"),

            "Quais cosméticos": input("\nQuais cosméticos são utilizados? (Deixe em branco se não houver)\n"),

            "Exposição ao sol": input("\nO paciente se expõe ao sol?\n"),

            "Frequência sol": input("\nCom que frequência se expõe ao sol?\n"),

            "Filtro solar": input("\nUsa filtro solar? (Deixe em branco se não pega sol)\n"),

            "Fumante": input("\nO paciente fuma?\n"),

            "Quantos cigarros": input("\nQuantidade de cigarros ao dia? (Deixe em branco se não fuma)\n"),

            "Bebida alcoólica": input("\nO paciente ingere bebida alcoólica?\n"),

            "Quanto bebe": input("\nCom qual a frequência ele bebe? (Deixe em branco se não bebe\n"),

            "Qualidade do sono": input("\nQual a qualidade do sono do paciente? (Boa, Regular, Péssima)\n"),

            "Horas de sono": input("\nQuantas horas de sono por dia?\n"),

            "Água": input("\nQuanta água o paciente bebe ao dia? (em copos/litros)\n"),

            "Alimentação": input("\nQualidade da alimentação? (Boa, Regular, Péssima)\n"),

            "Atividade física": input("\nO paciente pratica atividades físicas?\n"),

            "Quais atividades": input("\nQuais atividades ele pratica? (Deixe em branco se não houver)\n"),

            "Frequencia atividades físicas": input("\nCom que frequência ele pratica as atividades físicas? (Deixe em branco se não houver)\n"),

            "Tratamento médico atual": input("\nO paciente está fazendo algum tratamento médico atualmente?\n"),

            "Qual tratamento": input("\nQuais tratamentos? (Deixe em branco se não houver)\n"),

            "Alergia": input("\nO paciente possui alguma alergia?\n"),

            "Qual alergia": input("\nQual alergia? (Deixe em branco se não houver)\n"),

            "Marcapasso": input("\nO paciente é portador de marcapasso?\n"),

            "Alteração cardiaca": input("\nO paciente possui alguma alteração cardíaca?\n"),

            "Qual ateração cardíaca": input("\nQual alteração cardíaca? (Deixe em branco se não houver)\n"),

            "Pressão arterial": input("\nO paciente possui Hipo/Hipertensão arterial?\n"),

            "Distúrbio circulatório": input("\nO paciente possui algum problema circulatório?\n"),

            "Qual circulatório": input("\nQual distúrbio circulatório? (Deixe em branco se não houver)\n"),

            "Distúrbio renal": input("\nO paciente possui algum distúrbio renal?\n"),

            "Qual renal": input("\nQual distúrbio renal? (Deixe em branco se não houver)\n"),

            "Distúrbio hormonal": input("\nO paciente possui algum distúrbio hormonal?\n"),

            "Qual hormonal": input("\nQual distúrbio hormonal? (Deixe em branco se não houver)\n"),

            "Epilepsia/convulsão": input("\nO paciente sofre de epilepsia ou convulsões?\n"),

            "Frequencia epilepsia": input("\nCom que frequência? (Deixe em branco se não houver)\n"),

            "Alterações psicológicas": input("\nO paciente possui alguma alteração psicológica?\n"),

            "Qual psicológica": input("\nQual alteração psicológica? (Deixe em branco se não houver)\n"),

            "Estresse": input("\nO paciente sofre com estresse?\n"),

            "Estresse porque": input("\nQuais os motivos do estresse? (Deixe em branco se não houver)\n"),

            "Antecedentes oncológicos": input("\nO paciente possui algum antecedente oncológico? (Câncer, Tumor)\n"),

            "Qual oncológico": input("\nQual antecedente oncológico? (Deixe em branco se não houver)\n"),

            "Data oncológico": input("\nQuanto tempo faz? (Deixe em branco se não houver)\n"),

            "Diabete": input("\nO paciente possui diabetes?\n"),

            "Qual diabete?": input("\nQual o tipo de diabetes? (Deixe em branco se não houver)\n"),

            "Doença": input("\nO paciente sofre com algum outro tipo de doença?\n"),

            "Qual doença": input("\nQual doença? (Deixe em branco se não houver)\n"),
        }

        self.dados = dados

    def termo_responsabilidade(self):
        pass

    def teste(self):
        dados = {
            "nome": input("\nNome\n"),
            "idade": input("\nIdade\n"),
            "genero": input("\nGenero\n"),
        }
        self.dados = dados

    def acessar(self):
        while True:
            confirmar = input("\nDeseja alterar alguma informação? (Sim, Nao)\n")
            if confirmar == "Sim":
                dados = list(self.dados)
                dados.append("Não desejo alterar mais nada")
                cont = 1
                print("")
                for i in dados:
                    print(f"{cont} {i}")
                    cont += 1
                opcao = int(input("\nDigite a opção que deseja alterar:\n"))
                if dados[opcao - 1] == "Não desejo alterar mais nada":
                    return
                else:
                    self.dados[dados[opcao - 1]] = input(f"\n{dados[opcao - 1]}:\n")
                    self.apresentar()
            else:
                return

    def apresentar(self):
        # print(key e o value)
        #list(self.dados) = lista com cada key do dicionário
        #self.dados[key] = retorna o valor da key no dicionário
        print("\nPOR FAVOR CONFIRME OS DADOS\n")
        for i in list(self.dados):
            print(f"{i}: {self.dados[i]}")


class Salvar_pdf(Ficha_anamnese):
    def __init__(self):
        super().__init__()
        dados = self.dados

    def salvar(self):
        pass


if __name__ == "__main__":
    ficha = Ficha_anamnese()
    salvar = Salvar_pdf()
    ficha.teste()
    ficha.apresentar()
    ficha.acessar()