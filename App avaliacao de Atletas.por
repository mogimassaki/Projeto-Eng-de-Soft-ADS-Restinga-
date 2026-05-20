programa {

  // Função 1 — Calcula e retorna o valor numérico do IMC
  funcao real calcularIMC(real peso, real altura) {
    real imc = peso / (altura * altura)
    retorne imc
  }

  // Função 2 — Analisa o IMC e retorna o texto da classificação
  funcao cadeia classificarIMC(real imc) {
    se (imc < 18.5) {
      retorne "Abaixo do peso"
    } senao se (imc < 25.0) {
      retorne "Peso normal"
    } senao se (imc < 30.0) {
      retorne "Sobrepeso"
    } senao {
      retorne "Obesidade"
    }
  }

  // Função 3 — Analisa a frequência e retorna o texto do condicionamento
  funcao cadeia classificarCondicionamento(inteiro aulas) {
    se (aulas < 4) {
      retorne "Insuficiente"
    } senao se (aulas < 8) {
      retorne "Regular"
    } senao se (aulas < 12) {
      retorne "Bom"
    } senao {
      retorne "Excelente"
    }
  }

  // Função 4 — Recebe todos os dados processados e formata a tela
  funcao exibirRelatorio(cadeia nome, real imc, cadeia classIMC,
                         inteiro aulas, cadeia classCond) {
    escreva("\n--- RELATÓRIO DO ALUNO ---\n")
    escreva("Nome: ", nome, "\n")
    escreva("IMC: ", imc, " (", classIMC, ")\n")
    escreva("Aulas no mês: ", aulas, " (", classCond, ")\n")
    escreva("-------------------------\n\n")
  }

  funcao inicio() {
    cadeia nome
    real peso, altura, imc
    inteiro aulas
    inteiro excelente = 0
    
    // Variáveis criadas para armazenar os retornos das funções
    cadeia classIMC
    cadeia classCond

    para (inteiro i = 1; i <= 3; i++) {
      escreva("=== Aluno ", i, " ===\n")
      escreva("Nome: ")
      leia(nome)
      escreva("Peso (kg): ")
      leia(peso)
      escreva("Altura (m): ")
      leia(altura)
      escreva("Aulas no mes: ")
      leia(aulas)

      // Executa os cálculos salvando os resultados nas variáveis
      imc = calcularIMC(peso, altura)
      classIMC = classificarIMC(imc)
      classCond = classificarCondicionamento(aulas)

      // Chama o relatório passando as variáveis preenchidas
      exibirRelatorio(nome, imc, classIMC, aulas, classCond)
      
      // Incrementa excelente se a classificação for correspondente
      se (classCond == "Excelente") {
        excelente = excelente + 1
      }
    }

    // Exibe o total acumulado ao fim do laço para os 3 alunos
    escreva("Total de alunos com condicionamento Excelente: ", excelente, "\n")
  }
}