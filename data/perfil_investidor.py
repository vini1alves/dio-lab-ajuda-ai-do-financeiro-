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
print(f"O objetivo de {usuario['nome']} é {usuario['objetivo_principal']}.")
