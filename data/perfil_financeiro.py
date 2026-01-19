usuario = {
    "nome": "João Silva",
    "idade": 32,
    "profissao": "Analista de Sistemas",
    "renda_mensal": 5000.00,
    "perfil_investidor": "moderado",
    "objetivo_principal": "Construir reserva de emergência",
    "patrimonio_total": 15000.00,
    "reserva_emergencia_atual": 10000.00,
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
            "prazo": "2027-12"
        }
    ]
}

# Exemplo de como acessar um dado:
print(f"O objetivo de {usuario['nome']} é {usuario['objetivo_principal']}.")
