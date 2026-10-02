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

- `agente_suporte_ti.py` — agente principal com lógica de decisão, validação e integração com o modelo;
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

- uma API OpenAI-compatível, como OpenAI, Groq, Gemini ou Ollama;
- chamadas HTTP para o modelo via `requests`;
- lógica local para validação e self-consistency.

## Requisitos

- Python 3.10 ou superior
- pip
- acesso a um provedor de IA compatível com OpenAI (ex.: Ollama local, OpenAI, Groq, Gemini)

## Instalação

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install requests
```

Se você for usar a biblioteca OpenAI diretamente em outra versão do código, também pode instalar:

```bash
pip install openai
```

## Variáveis de ambiente

O projeto lê variáveis de ambiente para se conectar ao modelo.

### Exemplo usando Ollama local

```bash
set LLM_BASE_URL=http://localhost:11434/api/chat
set LLM_MODEL=qwen3.5:4b
```

### Exemplo usando OpenAI

```bash
set LLM_API_KEY=sk-...
set LLM_MODEL=gpt-4o-mini
```

### Exemplo usando Groq

```bash
set LLM_API_KEY=gsk_...
set LLM_BASE_URL=https://api.groq.com/openai/v1
set LLM_MODEL=llama-3.3-70b-versatile
```

### Exemplo usando Gemini

```bash
set LLM_API_KEY=...
set LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
set LLM_MODEL=gemini-2.0-flash
```

> Em sistemas Linux/macOS, troque `set` por `export`.

## Execução

Na pasta do projeto:

```bash
python agente_suporte_ti.py
```

## Observações importantes

- O código depende da biblioteca `requests` para enviar requisições ao modelo.
- Se o erro `ModuleNotFoundError: No module named 'requests'` aparecer, significa que a dependência ainda não foi instalada no ambiente correto.
- Para rodar corretamente, o ambiente Python do VS Code e o ambiente do terminal devem ser o mesmo.
- O Ollama precisa estar em execução localmente quando usado como backend padrão.

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
