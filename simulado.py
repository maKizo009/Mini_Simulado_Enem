import time

#while True:

time.sleep(1)
print("\n\n-------------------------------------------------------MINI SIMULADO PARA ENEM-------------------------------------------------------\n\n")    
time.sleep(1)
print("-------------------------------------------------------REGRAS:-------------------------------------------------------\n")
time.sleep(1)
print("Você pode adicionar letra maiúscula ou minúscula para a resposta que acha correta, mas se adicionar outros caracteres ou letras, pode ser que o programa quebre. Na dúvida, evite!\n\n")
time.sleep(2.5)
print("PRETENDO ADICIONAR MAIS FUNÇÕES EM BREVE, INCLUSIVE UM SISTEMA DE PONTUAÇÃO E MAIS PERGUNTAS. DIVIRTA-SE!!!\n\n")
time.sleep(2.5)

print("------------------------------------------------------História:------------------------------------------------------\n")
time.sleep(0.5)
historia = input("Qual foi o movimento artístico que surgiu na Europa no século XIV e se caracterizou pela valorização da cultura clássica greco-romana, do racionalismo e do humanismo?\n a) Barroco;\n b) Romantismo;\n c) Renascimento;\n d) Surrealismo;/n e)Expensionismo\n\n--------------------------------Escolha uma das alternativas: A, B, C, D, E--------------------------------:\n\n")
time.sleep(1)

print("------------------------------------------------------Química:------------------------------------------------------\n")
quimica = input("Qual é o nome do processo químico que ocorre quando uma substância orgânica é queimada na presença de oxigênio, produzindo gás carbônico e água?\n a) Combustão;\n b) Fermentação;\n c) Oxidação;\n d) Fotossíntese;\n e) Respiração\n\n--------------------------------Escolha uma das alternativas: A, B, C, D, E--------------------------------:\n\n")

time.sleep(1)

print("------------------------------------------------------Português:------------------------------------------------------\n")
portugues = input("Qual é a figura de linguagem que consiste em atribuir características humanas a seres não humanos?\n a) Metáfora;\n b) Metonímia;\n c) Prosopopeia;\n d) Hipérbole;\n e) Eufemismo\n\n--------------------------------Escolha uma das alternativas: A, B, C, D, E--------------------------------:\n\n")
time.sleep(1)

print("------------------------------------------------------Matemática:------------------------------------------------------\n")
matematica = input("Qual é a fórmula para calcular a área de um triângulo retângulo?\n a) A = b x h / 2;\n b) A = b x h;\n c) A = b² + h²;\n d) A = b² - h²;\n e) A = b x h / 4\n\n--------------------------------Escolha uma das alternativas: A, B, C, D, E--------------------------------:\n\n")

time.sleep(1)

print("------------------------------------------------------Redação------------------------------------------------------")

redacao = input("Qual é o tipo textual exigido na prova de redação do ENEM?\n a) Dissertativo-argumentativo;\n b) Narrativo-descritivo;\n c) Injuntivo-explicativo;\n d) Expositivo-comparativo;\n e) Dialogal-informativo\n\n--------------------------------Escolha uma das alternativas: A, B, C, D, E--------------------------------:\n")
time.sleep(1)
print("------------------------------------------------------FIM DO SIMULADO------------------------------------------------------\n")
time.sleep(1)

if historia.upper() == "C":
    nota1 = 200
else:
    nota1 = 0

if quimica.upper() =="A":
    nota2 = 200
else:
    nota2 = 0

if portugues.upper() == "C":
    nota3 = 200
else:
    nota3 = 0

if matematica.upper() == "A":
    nota4 = 200
else:
    nota4 = 0

if redacao.upper() == "A":
    nota5 = 200
else:
    nota5 = 0

soma = nota1 + nota2 + nota3 + nota4 + nota5


print("------------------------------------------------------A SUA NOTA SAI EM... 5------------------------------------------------------\n\n")
time.sleep(1)
print("4{}")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(2)
print("...")
time.sleep(0.1)

if soma == 0:
     print("------------------------------------------------REPROVADO!!! Lamentável...------------------------------------------------")
     time.sleep(0.5)
     print("UMA PENA, MAS VOCÊ ERROU TODAS AS QUESTÕES ;(\n\n")
elif soma > 0 and soma < 600:
    print("Que pena, você não passou, precisa estudar mais, sua nota foi de {} pontos\n\n".format(soma))
elif soma == 600:
        print("Você foi bem, tirou {} pontos\n\n".format(soma))
else:
        print("Meus parabéns! Você conseguiu {} pontos. Continue melhorando que você vai passar no ENEM!\n\n".format(soma))
time.sleep(0.5)

"""repetir = "S" 
while repetir == "S":
     repetir = input("Você deseja repetir o simulado? Responda com S para sim e N para não: ").upper()
     time.sleep(1)
     if repetir not in ["S", "N"]:
          print("Resposta inválida! Tente novamente com S ou N.")
          repetir = input("Você deseja repetir o simulado? Responda com S para sim e N para não: ").upper()
     elif repetir == "N":
          print("Obrigado por fazer o simulado, até mais!")
          break
     else:
          repetir"""
print("------------------------------------------------FIM DO PROGRAMA------------------------------------------------")