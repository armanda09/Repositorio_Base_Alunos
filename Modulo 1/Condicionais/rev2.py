nome = input("Nome do sistema de IA: ")
pontuacao = float(input("Pontuação de performance: "))

if pontuacao >= 0 and pontuacao <= 39.9:
    print("Sistema: ", nome,"Pontuação: ", pontuacao, "Classificação: IA em Treinamento🍼")
elif pontuacao >= 40.0 and pontuacao <= 69.9:
    print("Sistema: ", nome,"Pontuação: ", pontuacao, "Classificação: IA Intermediária🧠")
elif pontuacao >= 70.0 and pontuacao <= 89.9:
    print("Sistema: ", nome,"Pontuação: ", pontuacao, "Classificação: IA Otimizada🚀")
elif pontuacao >= 90.0 and pontuacao <= 100.0:
    print("Sistema: ", nome,"Pontuação: ", pontuacao, "Classificação: IA Avançada (nível Skynet)🤯")
elif pontuacao > 100:
    print("Sistema: ", nome,"Pontuação: ", pontuacao, "Classificação: IA Fora da escala!⚠️")
else:
    print("Sistema: ", nome,"Pontuação: ", pontuacao, "Erro: Pontuação inválida!❌")