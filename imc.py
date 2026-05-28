def calcular_imc(peso, altura):
    return peso / (altura * altura)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


def classificar_condicionamento(aulas):
    if aulas >= 20:
        return "Excelente"
    elif aulas >= 15:
        return "Bom"
    elif aulas >= 10:
        return "Regular"
    else:
        return "Fraco"


# ALTERAÇÃO: Nova função adicionada para gerar a mensagem com base no IMC
def mensagem_motivacional(class_imc):
    if class_imc == "Peso normal":
        return "Excelente trabalho! Continue mantendo seus hábitos saudáveis."
    else:
        return "Foco e constância! Cada treino aproxima você do seu objetivo."


# ALTERAÇÃO: Adicionado o parâmetro 'motivacao' na assinatura da função
def exibir_relatorio(nome, imc, class_imc, aulas, class_cond, motivacao):
    print("\n ---RELATÓRIO---")
    print("Nome", nome)
    print(f"IMC: {imc:.2f}")
    print("Classificação IMC:", class_imc)
    print("Aulas do mês:", aulas)
    print("Condicionamento:", class_cond)
    # ALTERAÇÃO: Adicionada a linha para exibir a mensagem no relatório impresso
    print("Mensagem:", motivacao)
    print("------------------\n")


excelente = 0

for i in range(1, 4):
    print(f"===Aluno {i}===")
    nome = input("Nome: ")
    peso = float(input("Peso (ex: 80): "))

    while peso <= 0:
        print("Peso inválido!")
        peso = float(input("Digite novamente: "))

    altura = float(input("Altura (ex: 1.80): "))
    aulas = int(input("Aulas no mês: "))

    imc = calcular_imc(peso, altura)
    class_imc = classificar_imc(imc)
    class_cond = classificar_condicionamento(aulas)
    # ALTERAÇÃO: Chamada da nova função para armazenar a mensagem na variável
    motivacao = mensagem_motivacional(class_imc)

    # ALTERAÇÃO: Atualizada a chamada da função para enviar a 'motivacao' como argumento
    exibir_relatorio(nome, imc, class_imc, aulas, class_cond, motivacao)

    if class_cond == "Excelente":
        excelente += 1

print("Total de alunos com condicionamento Excelente:", excelente)