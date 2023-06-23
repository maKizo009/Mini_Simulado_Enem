import time
import os
repetir = "S"
while repetir == "S":
    #materias = historia, quimica, matematica, portugues, redacao
    enunciado = "-" *50 + "Escolha uma das alternativas: A, B, C, D, E: " + "-" * 50 + "\n"
    def Traços(materia):
        print("-" * 50, materia, "-" * 50, "\n")
    def alternativas(enunciado):
        return enunciado
#    def respsErradas(materia):
#        while materias.upper() != ["A", "B", "C" "D", "E"]:
#            print("Resposta inválida!!! Responda com A, B, C, D ou E")
#            historia = input(f"""Qual foi o movimento artístico que surgiu na Europa no século XIV e se caracterizou pela valorização da cultura clássica greco-romana, do racionalismo e do humanismo?
#            |
#            |a) Barroco;
#            |b) Romantismo;
#            |c) Renascimento;
#            |d) Surrealismo;
#            |e)Expensionismo.
#            {alternativas(enunciado)}
#            |R: """
#            os.system('cls')

    Traços("MINI SIMULADO PARA O ENEM")    
    Traços("REGRAS:")
    time.sleep(0.3)
    print("""Você pode adicionar letra maiúscula ou minúscula para a resposta que acha correta, mas se adicionar outros caracteres ou letras, pode ser que o programa quebre. Na dúvida, evite!
    PRETENDO ADICIONAR MAIS FUNÇÕES EM BREVE, INCLUSIVE UM SISTEMA DE PONTUAÇÃO E MAIS PERGUNTAS. DIVIRTA-SE!!!""")
    time.sleep(0.3)
    Traços("História")
    historia = input(f"""Qual foi o movimento artístico que surgiu na Europa no século XIV e se caracterizou pela valorização da cultura clássica greco-romana, do racionalismo e do humanismo?
    |
    |a) Barroco;
    |b) Romantismo;
    |c) Renascimento;
    |d) Surrealismo;
    |e)Expensionismo.
    {alternativas(enunciado)}
    |R: """)

    time.sleep(0.3)
    Traços("Química")
    quimica = input(f"""Qual é o nome do processo químico que ocorre quando uma substância orgânica é queimada na presença de oxigênio, produzindo gás carbônico e água?
    a) Combustão;
    b) Fermentação;
    c) Oxidação;
    d) Fotossíntese;
    e) Respiração.
    {alternativas(enunciado)}
    R: """)

    time.sleep(0.3)
    Traços("Português")
    portugues = input(f"""Qual é a figura de linguagem que consiste em atribuir características humanas a seres não humanos?
    a) Metáfora;
    b) Metonímia;
    c) Prosopopeia;
    d) Hipérbole;
    e) Eufemismo.
    {alternativas(enunciado)}
    R: """)
    time.sleep(0.3)
    Traços("Matemática")
    matematica = input(f"""Qual é a fórmula para calcular a área de um triângulo retângulo?
    a) A = b x h / 2;
    b) A = b x h;
    c) A = b² + h²;
    d) A = b² - h²;
    e) A = b x h / 4.
    {alternativas(enunciado)}
    R: """)

    time.sleep(0.3)
    Traços("Redação")
    redacao = input(f"""Qual é o tipo textual exigido na prova de redação do ENEM?
    a) Dissertativo-argumentativo; 
    b) Narrativo-descritivo;
    c) Injuntivo-explicativo;
    d) Expositivo-comparativo;
    e) Dialogal-informativo.
    {alternativas(enunciado)}
    R: """)
    time.sleep(0.5)
    Traços("FIM DO SIMULADO")
    time.sleep(0.5)

    resultados = []
    if historia.upper() == "C":
        nota1 = 200
        resultados.append("História")
    else:
        nota1 = 0
    if quimica.upper() =="A":
        nota2 = 200
        resultados.append("Química")
    else:
        nota2 = 0
    if portugues.upper() == "C":
        nota3 = 200
        resultados.append("Português")
    else:
        nota3 = 0
    if matematica.upper() == "A":
        nota4 = 200
        resultados.append("Matemática")
    else:
        nota4 = 0
    if redacao.upper() == "A":
        nota5 = 200
        resultados.append("Redação")
    else:
        nota5 = 0
    soma = nota1 + nota2 + nota3 + nota4 + nota5

    Traços("A SUA NOTA SAI EM...")
    time.sleep(1)
    Traços("3")
    time.sleep(1)
    Traços("2")
    time.sleep(1)
    Traços("1")
    time.sleep(1)
    Traços("...")
    time.sleep(0.5)

    if soma == 0:
        Traços("REPROVADO!!! LAMENTÁVEL...")
        time.sleep(0.5)
        print("UMA PENA, MAS VOCÊ ERROU TODAS AS QUESTÕES ;(\n\n")
    elif soma > 0 and soma < 600:
        print("Que pena, você não passou, precisa estudar mais, sua nota foi de {} pontos\n\n".format(soma))
        print("As questões que você acertou foram: {}".format(", ".join(resultados)))
    elif soma == 600:
        print("Você foi bem, tirou {} pontos\n\n".format(soma))
        print("As questões que você acertou foram: {}".format(", ".join(resultados)))
    else:
        print("Meus parabéns! Você acertou todas as questões e conseguiu {} pontos. Continue melhorando que você vai passar no ENEM!\n\n".format(soma))
        time.sleep(0.5)

    repetir = input("Você deseja repetir o simulado? Responda com S para sim e N para não: ").upper()
    time.sleep(0.3)
    while repetir not in ["S", "N"]:
        print("Resposta inválida! Tente novamente com S ou N.")
        repetir = input("Você deseja repetir o simulado? Responda com S para sim e N para não: ").upper()
    if repetir == "N":
        print("Obrigado por fazer o simulado, até mais!")
        break
    else:
        repetir
    Traços("FIM DO PROGRAMA!")
