# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
google.generativeai
pandas
```

## Como Rodar

```bash
# Instalar dependências
pip install streamlit 

# Rodar a aplicação
streamlit run DIO/app.py
```
