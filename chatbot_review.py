# Chatbot interativo para analisar a review de um cliente

review_cliente = '''Este soprador de folhas é bastante incrível. Ele tem
quatro configurações: sopro de vela, brisa suave, cidade ventosa
e tornado. Chegou em dois dias, bem a tempo para o presente de
aniversário da minha esposa. Acho que minha esposa gostou tanto
que ficou sem palavras. Até agora, fui o único a usá-lo, e tenho
usado em todas as manhãs alternadas para limpar as folhas do
nosso gramado. É um pouco mais caro do que os outros sopradores
de folhas disponíveis no mercado, mas acho que vale a pena pelas
características extras.'''

# Função simulando um chatbot com respostas simples
def chatbot(pergunta):
    pergunta = pergunta.lower()

    if "produto" in pergunta:
        return "\n🛠 Produto: O cliente descreveu o produto como “incrível”, elogiou as configurações e considerou o valor justo pelas características."

    elif "entrega" in pergunta:
        return "\n📦 Entrega: O cliente recebeu o produto em dois dias, antes do aniversário da esposa, e parece satisfeito com a entrega."

    elif "atendimento" in pergunta:
        return "\n🤝 Atendimento: Não há menção específica ao atendimento, logo não é possível avaliar."

    elif "satisfacao" in pergunta or "satisfação" in pergunta:
        return "\n😊 Satisfação geral: O cliente está satisfeito com a compra como um todo, destacando funcionalidades e entrega."

    else:
        return "\nDesculpe, não entendi a pergunta. Digite: produto, entrega, atendimento ou satisfação."

# Loop interativo
print("\nOlá! Digite sobre o que você deseja saber (produto, entrega, atendimento ou satisfacao). Digite 'sair' para encerrar.")

while True:
    entrada = input("\nSua escolha: ").strip().lower()
    if entrada == "sair":
        print("\nAté a próxima!")
        break
    resposta = chatbot(entrada)
    print(resposta)
