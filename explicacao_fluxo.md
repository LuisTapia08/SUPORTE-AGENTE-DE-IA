# Agente de Suporte de TI – Explicação do fluxo

## Ideia central: decomposição LLM ↔ Python
O modelo **decide**, o Python **executa**. A cada mensagem do funcionário:

```
Funcionário ──► [1. LLM DECISOR, temp 0] ──JSON──► [2. PYTHON valida]
                                                     ├─ responder  → mostra a resposta
                                                     ├─ propor     → self-consistency → guarda PENDENTE → pede confirmação
                                                     ├─ confirmar  → abrir_chamado() (+ notificar_equipe() se alta)
                                                     │                 └─► [3. LLM REDATOR] com o número REAL
                                                     └─ cancelar   → descarta o pendente
```

## Respostas às perguntas do enunciado
1. **O que o LLM decide e em que formato?** Uma `acao` entre `responder`, `propor`, `confirmar` e `cancelar`, num JSON:
   `{"acao": ..., "resposta": ..., "chamado": {"categoria", "prioridade", "resumo"}}`. O `response_format=json_object` e a temperatura 0 deixam a saída estável.
2. **O que o Python faz?** Lê o JSON, valida categoria/prioridade contra as listas oficiais, corta o resumo em 10 palavras e só então chama as funções de `ferramentas_triagem.py`.
3. **Como o agente sabe da confirmação?** O chamado proposto fica na variável `pendente` do Python, que é enviada ao decisor em todo turno como "ESTADO DO SISTEMA". O modelo só pode escolher `confirmar` se houver pendente, e o Python verifica isso de novo antes de executar. Correção ("na verdade é o 4º andar") vira um novo `propor` que substitui o pendente; "não" vira `cancelar`.
4. **Como o resultado volta para a conversa?** O número retornado por `abrir_chamado()` é passado a um segundo prompt (redator), que escreve a resposta natural. O Python confere se o texto tem exatamente esse número; se não tiver (ou tiver outro), usa uma frase padrão. Assim o número nunca é inventado (regra 6). A resposta final entra no histórico.
5. **Quantas chamadas e quais prompts?** Três prompts diferentes, cada um com um papel:
   - **Decisor** (temp 0): sempre, a cada mensagem.
   - **Classificador** (temp 0.8, 3 amostras): só ao propor um chamado. É a **self-consistency**: voto da maioria para categoria e prioridade, reforçando a regra 8 (prioridade pelo impacto, não pelo tom).
   - **Redator** (temp 0.5): só depois de abrir um chamado.

## Requisitos atendidos
- **System prompt** com papel, contexto (categorias/prioridades), formato (JSON) e restrições (regras 1–10, proteção contra prompt injection).
- **Histórico** enviado inteiro ao decisor em toda mensagem.
- **Tratamento de erro**: JSON inválido → extração por regex → nova tentativa pedindo o formato correto → mensagem segura. Falha de API não derruba o programa. Valores fora das listas são rejeitados.
- **Critério de parada**: digitar `sair` (ou Ctrl+C).
- **Regra 5**: `notificar_equipe()` só quando a prioridade final for `alta`, depois de abrir o chamado.
