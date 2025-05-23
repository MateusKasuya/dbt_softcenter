yaml = f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_{schema}_tbcli # Nome do modelo
    description: "View Staging da TBCLI"  # Descrição do modelo
    columns:
          - name: cgccpfcli
            description: CPF/CNPJ Cliente - Primary Key

          - name: nomefantasia
            description: Nome Fantasia Cliente


"""