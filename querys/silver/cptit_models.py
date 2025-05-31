def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_cptit # Nome do modelo
    description: "View Silver da CPTIT"  # Descrição do modelo
    columns:
      - name: nrocontrole
        description: Número CTRC - Primary Key Composta

      - name: anocontrole
        description: Ano CTRC - Primary Key Composta

      - name: codfil
        description: Código Filial - FK TBFIL

      - name: cgccpfforne
        description: CPF/CNPJ Fornecedor - FK TBCLI

      - name: codtransacao
        description: Código Transação - FK TBPRO

      - name: vlrtotal
        description: Valor Total

      - name: vlrpago
        description: Valor Saldo

      - name: vlrsaldo
        description: Valor Saldo

      - name: dataemissao
        description: Data Emissão

      - name: datamovto
        description: Data Movimento

      - name: datavencto
        description: Data Vencimento

      - name: condicao_fatura
        description: Condição Fatura

      - name: contareduz
        description: Conta de Pagamento
"""
