# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `projeto3.py` | PYTHON | Codigo principal |
| `perfil_investidor.py` | PYTHON | Perfil do clientes |
| `produtos_financeiro.py` | PYTHON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> alterei os arquivos de json para python e importei os arquivos .py para projeto principal!

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Eu alterei o alguns dados do perfil e do produto eu mudei o tipo de arquivo json para python.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

```python
import pandas as pd
from perfil_investidor import usuario
from produtos_financeiro import investimentos

transacao = pd.read_csv("transacoes.csv")
usuario
investimentos
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```python
usuario = {
    "nome": "João Silva",
    "idade": 45,
    "profissao": "auxiliar operacional",
    "renda_mensal": 2300.00,
    "perfil_investidor": "moderado",
    "objetivo_principal": "Construir um plano de investimento",
    "patrimonio_total": 5000.00,
    "reserva_emergencia_atual": 3000.00,
    "aceita_risco": False,
    "metas": [
        {
            "meta": "Concluir reserva de emergência",
            "valor_necessario": 15000.00,
            "prazo": "2026-06"
        },
        {
            "meta": "Entrada do apartamento",
            "valor_necessario": 50000.00,
            "prazo": "2035-12"
        }
    ]
}

# Exemplo de como acessar um dado:
#print(f"O objetivo de {usuario['nome']} é {usuario['objetivo_principal']}.")
```
```python
investimentos = [
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% a 105% do CDI",
    "aporte_minimo": 1.00,
    "indicado_para": "Quem busca segurança com rendimento diário e reserva de emergência"
  },
  {
    "nome": "CDB Pós-fixado (Vencimento Longo)",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "110% a 120% do CDI",
    "aporte_minimo": 1.00,
    "indicado_para": "Investidores que buscam maximizar o retorno acompanhando a taxa Selic"
  },
  {
    "nome": "CDB Prefixado",
    "categoria": "renda_fixa",
    "risco": "médio (risco de custo de oportunidade)",
    "rentabilidade": "Taxa fixa (ex: 12% ao ano)",
    "aporte_minimo": 50.00,
    "indicado_para": "Quem acredita que a taxa de juros (Selic) vai cair no futuro"
  },
  {
    "nome": "CDB IPCA+ (Híbrido)",
    "categoria": "renda_fixa",
    "risco": "baixo/médio",
    "rentabilidade": "IPCA + 6% ao ano (exemplo)",
    "aporte_minimo": 500.00,
    "indicado_para": "Proteção contra a inflação e manutenção do poder de compra a longo prazo"
  },
  {
    "nome": "CDB Escalonado (Progressivo)",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "Crescente (ex: de 100% a 115% do CDI)",
    "aporte_minimo": 1.00,
    "indicado_para": "Quem quer liquidez, mas deseja prêmios maiores por deixar o dinheiro investido por mais tempo"
  },
  {
    "nome": "CDB de Banco Médio/Pequeno",
    "categoria": "renda_fixa",
    "risco": "médio (coberto pelo FGC)",
    "rentabilidade": "115% a 130% do CDI",
    "aporte_minimo": 500.00,
    "indicado_para": "Investidores que buscam rentabilidade agressiva em renda fixa aceitando menor liquidez"
  }
]

# Exemplo: Filtrar apenas investimentos de baixo risco
'''baixo_risco = [i["nome"] for i in investimentos if i["risco"] == "baixo"]
print(f"Opções seguras: {baixo_risco}")'''

```
```CSV
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,2300.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

```
```python
nome_lista = usuario["nome"]

while True:
    tentar = (input("digite o nome do cliente:").strip())


    if  tentar.title() == nome_lista:
        print(f"acesso permitido{nome_lista}.")
        break
    else:
        print(f"nome incorreto tente novamente")

print("--resumo do cliente--")
print(f"Dados do cliente:")
print(f" nome: {usuario['nome']}")
print(f"- Perfil: {usuario['perfil_investidor'].capitalize()}")
print(f"- Saldo disponível: R$ {usuario['patrimonio_total']:,.2f}")

print("\nÚltimas transações:")

ultimas_transacoes = transacao.tail(5)
for index, linha in ultimas_transacoes.iterrows():
    # Convertendo a data para o formato brasileiro (DD/MM)
    data_formatada = pd.to_datetime(linha['data']).strftime('%d/%m')
    
    print(f"- {data_formatada}: {linha['descricao']} - R$ {linha['valor']:.2f}")
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
nome incorreto tente novamente
acesso permitidoJoão Silva.
--resumo do cliente--
Dados do cliente:
 nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5,000.00

Últimas transações:
- 10/10: Restaurante - R$ 120.00
- 12/10: Uber - R$ 45.00
- 15/10: Conta de Luz - R$ 180.00
- 20/10: Academia - R$ 99.00
- 25/10: Combustível - R$ 250.00
...
```
