def get_yml_content() -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: calendario # Nome do modelo
    description: "Tabela Mart Calendario - extraída da CTE (FRCTRC)"  # Descrição do modelo
    columns:
          - name: data
            description: Data do Calendário - Primary Key

          - name: ano
            description: Ano da data

          - name: mes
            description: Mês da data

          - name: mes_nome
            description: Nome do mês da data

          - name: mes_ano
            description: Concatenado de Nome do mês e Ano

          - name: dia
            description: Dia da data

          - name: flag_ano_movel
            description: Flag para indicar se o ano é pertencente aos 3 últimos anos

          - name: flag_ano_atual
            description: Flag para indicar se o ano é o ano atual
"""
