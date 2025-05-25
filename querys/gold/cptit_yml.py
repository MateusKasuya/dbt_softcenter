def get_yml_content() -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: cptit # Nome do modelo
    description: "Tabela Gold da cptit"  # Descrição do modelo
    columns:
      - name: source
        description: Fonte de origem/ Empresa
    tests:
      - cptit_row_count:
          source_table: 'CPTIT'
          source_schema: fn9
          nome_empresa: FN9
      - cptit_sum_match:
          source_table: 'CPTIT'
          source_schema: fn9
          column_name: vlrtotal
          nome_empresa: FN9
      - cptit_row_count:
          source_table: 'CPTIT'
          source_schema: mgp
          nome_empresa: MGP
      - cptit_sum_match:
          source_table: 'CPTIT'
          source_schema: mgp
          column_name: vlrtotal
          nome_empresa: MGP
      - cptit_row_count:
          source_table: 'CPTIT'
          source_schema: rcr
          nome_empresa: RCR
      - cptit_sum_match:
          source_table: 'CPTIT'
          source_schema: rcr
          column_name: vlrtotal
          nome_empresa: RCR
"""
