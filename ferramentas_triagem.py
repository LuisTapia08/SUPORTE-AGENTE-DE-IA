import random

# Equipe responsável por cada categoria
EQUIPES = {
    "acesso": "Equipe de Segurança e Acessos",
    "hardware": "Equipe de Suporte Técnico",
    "rede": "Equipe de Infraestrutura",
    "software": "Equipe de Sistemas",
}


def abrir_chamado(categoria, prioridade, resumo):
    """
    Abre um chamado no sistema de suporte (simulado).
    Retorna o número do chamado criado.
    """
    numero = random.randint(1000, 9999)
    print(f"[SISTEMA] Chamado #{numero} aberto | {categoria} | prioridade {prioridade} | {resumo}")
    return numero


def notificar_equipe(categoria, mensagem):
    """
    Envia um aviso para a equipe responsável pela categoria (simulado).
    Retorna True se a notificação foi enviada.
    """
    equipe = EQUIPES.get(categoria)
    if equipe is None:
        print(f"[AVISO] Nenhuma equipe cadastrada para a categoria '{categoria}'.")
        return False

    print(f"[NOTIFICAÇÃO] Para: {equipe} | {mensagem}")
    return True


# Teste rápido
if __name__ == "__main__":
    numero = abrir_chamado("rede", "alta", "Setor financeiro sem internet desde 8h")
    notificar_equipe("rede", f"Chamado #{numero} de prioridade alta aguardando atendimento.")
