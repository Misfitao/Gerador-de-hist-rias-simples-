import random

def escolher_personagem():
    personagens = ["um dragão", "uma princesa", "um robô", "um pirata", "um vampiro"]
    return random.choice(personagens)

def escolher_local():
    locais = ["em uma floresta encantada", "em um castelo antigo", "em uma nave espacial", "em uma ilha deserta", "em uma cidade futurística"]
    return random.choice(locais)

def escolher_acao():
    acoes = ["encontrou um tesouro perdido", "lutou contra um monstro", "viajou no tempo", "fez um grande amigo", "desvendou um mistério"]
    return random.choice(acoes)

def gerar_historia():
    personagem = escolher_personagem()
    local = escolher_local()
    acao = escolher_acao()

    historia = f"Era uma vez {personagem} {local}, que {acao}."
    return historia

# Função principal
def jogo():
    print("Bem-vindo ao gerador de histórias!")
    input("Pressione Enter para gerar uma história...")

    historia = gerar_historia()
    print("\nAqui está a sua história:\n")
    print(historia)

# Executa o jogo
jogo()
