def get_yml_content(source: str) -> str:
    return f"""
version: 2

sources:
  - name: {source}
    description: "Essa é uma réplica do banco Firebird usado no Frete Fácil"
    database: postgres
    schema: {source}
    tables:
      - name: "FRCTRC"
        description: Movimento de CTRC's

      - name: "TBCID"
        description: Cadastro de Localidades/Cidades

      - name: "TBCLI"
        description: Cadastro de Clientes

      - name: "TBFIL"
        description: Cadastro de Filiais

      - name: "FACTRC"
        description: Movimento de Faturas

      - name: "CPTIT"
        description: Movimento de Contas a Pagar

      - name: "TBHIS"
        description: Cadastro de Históricos

      - name: "TBFOR"
        description: Cadastro de Fornecedores

      - name: "TBPRO"
        description: Cadastro de Produtos Transportados

      - name: "TBCTA"
        description: Cadastro de Contas a Receber
"""
