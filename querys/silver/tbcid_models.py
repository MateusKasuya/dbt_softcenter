def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_silver_tbcid # Nome do modelo
    description: "View Silver da TBCID"  # Descrição do modelo
    columns:
          - name: codcid
            description: Código Cidade - Primary Key

          - name: nome
            description: Nome Cidade

          - name: coduf
            description: UF Cidade

          - name: cidade_uf
            description: Concatenado de Cidade e UF

          - name: localizacao_pbi
            description: Campo para ser utilizado como Mapa no Power BI
"""
