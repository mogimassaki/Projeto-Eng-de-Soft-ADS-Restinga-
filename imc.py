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

def classificar_condicionamento (aulas):
    if aulas >= 20:
        return "Excelente"
    elif aulas >= 15:
        return "Bom"
    elif aulas >= 10:
        return "Regular"
    else:
        return "Fraco"

def exibir_relatorio(nome, imc, class_imc, aulas, class_cond):
    print("\n ---RELATÓRIO---")
    print("Nome", nome)
    print(f"IMC: {imc:.2f}")
    print("Classificação IMC:", class_imc)
    print("Aulas do mês:", aulas)
    print("Condicionamento:", class_cond)
    print("------------------\n")

excelente = 0

for i in range(1, 4):
    print(f"===Aluno {i}===")
    nome = input("Nome: ")
    peso = float(input("Peso (ex: 80): "))
    altura = float(input("Altura (ex: 1.80): "))
    aulas = int(input("Aulas no mês: "))
    imc = calcular_imc(peso, altura)
    class_imc = classificar_imc(imc)
    class_cond = classificar_condicionamento(aulas)
    exibir_relatorio(nome, imc, class_imc, aulas, class_cond)
    if class_cond == "Excelente":
        excelente += 1

print("Total de alunos com condicionamento Excelente:", excelente)