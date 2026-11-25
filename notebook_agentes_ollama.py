# Agentes com LangChain + Ollama local
# Agente "goat" (sotaque baiano) + pipeline PT -> JP (japones, romaji, dicionario JLPT)
import os
os.environ['LANGSMITH_TRACING'] = 'false'
os.environ['LANGCHAIN_TRACING_V2'] = 'false'
os.environ['OTEL_SDK_DISABLED'] = 'true'

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

modelo = ChatOllama(
    model='qwen3.5:4b',
    base_url='http://localhost:11434',
    temperature=0.2,
    reasoning=False,
    num_predict=1024,
    validate_model_on_init=False,
    client_kwargs={'timeout': 60}
)
print('Modelo configurado: qwen3.5:4b no Ollama local.')


# ---------- Agente goat (sotaque baiano) ----------
ogoat = create_agent(
    modelo,
    tools=[],
    system_prompt="Você é o goat, um agente que fala com sotaque baiano."
)

def chamar(agente, texto):
    resp = agente.invoke(
        {'messages': [{"role": "user", "content": texto}]},
        config={'recursion_limit': 8}
    )
    return resp['messages'][-1].text.strip()


user_input = input("Fale com o goat: ")
print(chamar(ogoat, user_input) or "O modelo não retornou texto para o goat.")


# ---------- Agentes de japones ----------
nihongo = create_agent(
    modelo,
    tools=[],
    system_prompt=(
        "Traduza do português para o japonês natural. Se o usuário perguntar como se diz "
        "uma frase entre aspas, traduza apenas essa frase. Responda só com a tradução. "
        "Preserve os nomes próprios: translitere para katakana sem mudar o nome. "
        "Por exemplo, Beatriz pode ser escrita ベアトリス. Na dúvida, mantenha a grafia original. "
        "Exemplo: 'como se diz \"eu gosto da Marina\" em japonês?' → マリナが好きです。 "
        "Para 'de todo o coração', use 心から."
    )
)
tradutor_romaji = create_agent(
    modelo,
    tools=[],
    system_prompt=(
        "Transcreva o texto japonês para romaji Hepburn, preservando todos os nomes e palavras. "
        "Transcreva as partículas は, を e へ como wa, o e e quando usadas como partículas. "
        "Exemplo: マリナを心から信じています。 → Marina o kokoro kara shinjite imasu. "
        "Responda apenas com o romaji."
    )
)
tradutor_dicionario = create_agent(
    modelo,
    tools=[],
    system_prompt=(
        "Explique em português as palavras japonesas comuns da frase, uma por linha. "
        "Use o formato palavra — leitura em hiragana — significado em português. "
        "Omita completamente os nomes próprios: não crie uma linha nem comente sobre eles. "
        "Explique expressões e verbos conjugados como unidades e omita partículas isoladas. "
        "Não invente etimologias. "
        "Se mencionar um nível JLPT, indique que é aproximado e omita-o quando tiver dúvida. "
        "Exemplo de entrada: マリナを心から愛しています。\n"
        "Exemplo de saída:\n心から — こころから — de todo o coração\n"
        "愛しています — あいしています — amo (forma polida)"
    )
)

while True:
    user_input = input("Digite em português (ou 'exit' para sair): ")
    if user_input.strip().lower() == "exit":
        break

    japones = chamar(nihongo, user_input)
    if not japones:
        print("O modelo não retornou a tradução. Tente digitar a frase novamente.")
        continue
    print(japones)

    print(chamar(tradutor_romaji, japones) or "O modelo não retornou o romaji.")
    print(chamar(tradutor_dicionario, japones) or "O modelo não retornou o vocabulário JLPT.")
    print("\n\n")
