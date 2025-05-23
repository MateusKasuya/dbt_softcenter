yaml = f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_{schema}_tbfil # Nome do modelo
    description: "View Staging da TBFIL"  # Descrição do modelo
    columns:
          - name: codfil
            description: Código Filial - Primary Key

          - name: nome
            description: Nome Filial


"""