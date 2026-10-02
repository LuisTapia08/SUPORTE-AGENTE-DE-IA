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
pip install requests
```

3. Verifique se o Ollama está instalado e execute um modelo local, por exemplo:

```bash
ollama run qwen3.5:4b
```

## Variáveis de ambiente

O projeto lê as seguintes variáveis para conectar ao Ollama local:

```bash
set LLM_BASE_URL=http://localhost:11434/api/chat
set LLM_MODEL=qwen3.5:4b
```

> Em sistemas Linux/macOS, troque `set` por `export`.

## Execução

Na pasta do projeto:

```bash
python agente_suporte_ti.py
```

## Observações importantes

- O código depende da biblioteca `requests` para enviar requisições ao modelo.
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
