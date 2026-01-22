''' meu computador nao consegui rodar o ollama com gpt-oss'''

import pandas as pd
import requests
import streamlit as st


#config
ollama_url= 'http://localhost:11434/api/generate'
MODELO = "gpt-oss"

#carregar dados
from perfil_investidor import usuario
from produtos_financeiro import investimentos

transacao = pd.read_csv("DIO/transacoes.csv")




#montar contexto 
contexto = f"""
CLIENTE: {usuario["nome"]}, {usuario["idade"]}anos, {usuario["perfil_investidor"]}
OBJETIVO: {usuario["obejetivo_principal"]}
PATRIMONIO: R$ {usuario["patrimoni_total"]} | RESERVA: {usuario["reserva_emergencia_atual"]}

TRANSAÇÕES RECENTES:
{transacao.to_string(index=False)}

PERFIL_INVESTIDOR:
{usuario}

PRODUTOS DISPONIVEIS:
{investimentos}

"""

#system prompt

SYSTEM_PROMPT = """ voce e um agente de finanças AJUDA-aí 

Exemplo de estrutura:
Você é um agente financeiro inteligente especializado em cdb.
Seu objetivo é ensinar sobre, impostos sobre o rendimento, pagamento de impostos de renda, cálculos, juros básicos.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Nunca passe senha de outros perfis
5. Não recomenda outros investimento que nao tiver no banco de dados
6. sempre indicar uma recomendação um profissional especializado em investimentos que nao estão no banco de dados.
"""


#chamar ollama

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO_CLIENTE:
    {contexto}
    pergunta: {msg}"""


    r = requests.post(ollama_url, json={"model": MODELO, "prompt": prompt, "stream":False})
    return r.json()["response"]


#interface

st.title("Olá e sou agente finaceiro AJUDA-aí")

if pergunta := st.chat_input(" Qual e a sua pergunta sobre!"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
