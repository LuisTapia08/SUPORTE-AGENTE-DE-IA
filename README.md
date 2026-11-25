# Agente de Suporte de TI

Projeto de um agente inteligente para atendimento de suporte interno de TI, com lógica de classificação de demandas, criação de chamados e fluxo de confirmação antes da abertura do ticket.

## Objetivo

O sistema simula um assistente de suporte para a Distribuidora Rio Negro, capaz de:

- analisar mensagens de funcionários;
- decidir se deve responder, propor um chamado, confirmar ou cancelar;
- classificar categoria e prioridade do problema;
- abrir chamados de suporte;
- notificar a equipe responsável;
- gerar resposta final em linguagem natural.

## Estrutura do projeto

- `agente_suporte_ti.py` — versão 1: o modelo devolve um JSON com a ação e o Python decide;
- `agente_tools.py` — versão 2: function calling com `TOOLS` e `TOOL_FUNCTIONS` (o modelo pede a ferramenta e o Python executa, com confirmação do funcionário);
- `ferramentas_triagem.py` — funções simuladas para abertura de chamados e notificação;
- `explicacao_fluxo.md` — descrição do fluxo do agente;
- `README.md` — documentação do projeto.

## Como funciona

O fluxo principal é:

1. O modelo decide a ação com base no histórico e no estado do sistema.
2. O Python valida a resposta JSON.
3. Se houver um problema claro, o agente propõe um chamado.
4. O usuário confirma ou cancela.
5. O sistema abre o chamado e gera uma resposta final ao funcionário.

O projeto usa:

- Ollama local como provedor de IA;
- requisições HTTP para o modelo via `requests`;
- lógica local para validação, auto-consistência e controle do fluxo.

## Requisitos

- Python 3.10 ou superior
- pip
- Ollama instalado e em execução localmente

## Instalação

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Deixe o Ollama aberto e confira os modelos instalados:

```bash
ollama --version
ollama list
```

Se não houver nenhum modelo, baixe um (ex.: `ollama pull qwen3:4b`).

## Configuração (opcional)

Copie `.env.example` para `.env` e ajuste se precisar:

| Variável | Padrão | Para que serve |
|---|---|---|
| `OLLAMA_URL` | `http://localhost:11434` | Endereço do Ollama |
| `LLM_MODEL` | vazio | Modelo a usar; vazio = o programa lista os modelos instalados para você escolher |
| `LLM_TIMEOUT` | `180` | Segundos de espera por resposta do modelo |
| `LLM_THINK` | `false` | Liga o "thinking" de modelos como qwen3 (mais lento) |
| `LLM_KEEP_ALIVE` | `30m` | Tempo que o modelo fica carregado na memória após o último uso |

Ao iniciar, o agente confere se o Ollama está rodando, mostra a versão e confirma o modelo. Se o modelo de `LLM_MODEL` não estiver instalado, ele avisa e deixa escolher outro.

## Execução

Na pasta do projeto:

```bash
python agente_suporte_ti.py   # versão 1 (JSON de decisão)
python agente_tools.py        # versão 2 (function calling)
```

## Observações importantes

- O código depende só da biblioteca `requests` para falar com o Ollama (API `/api/chat`).
- Se o erro `ModuleNotFoundError: No module named 'requests'` aparecer, instale a dependência no ambiente correto.
- O Ollama precisa estar ativo antes de iniciar o programa.
- Para rodar corretamente, o ambiente Python do VS Code e o ambiente do terminal devem ser os mesmos.

## Possíveis categorias de suporte

- `acesso`
- `hardware`
- `rede`
- `software`

## Possíveis prioridades

- `alta`
- `media`
- `baixa`

## Exemplos de ações do agente

- `responder` — conversa comum ou resposta genérica
- `propor` — sugere abertura de chamado
- `confirmar` — confirma a abertura do chamado pendente
- `cancelar` — descarta o chamado pendente

## Licença

Este projeto foi desenvolvido como exercício acadêmico de apoio ao aprendizado de agentes inteligentes e suporte de TI.
