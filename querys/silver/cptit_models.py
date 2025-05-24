def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_silver_cptit # Nome do modelo
    description: "View Silver da CPTIT"  # Descrição do modelo
    columns:
          - name: nrocontrole
            description: Número Controle - Primary Key

          - name: anocontrole
            description: Ano Controle - Primary Key

          - name: codfil
            description: Código Filial - FK TBFIL

          - name: cgccpfforne
            description: CPF/CNPJ Fornecedor - FK TBFOR

          - name: codtransacao
            description: Código Transação - FK TBHIS

          - name: vlrtotal
            description: Valor total a pagar

          - name: vlrpago
            description: Valor total pago

          - name: vlrsaldo
            description: Valor de saldo restante a pagar

          - name: dataemissao
            description: Data de emissão do documento

          - name: datamovto
            description: Data de Pagamento

          - name: datavencto
            description: Data de Vencimento do documento

          - name: condicao_fatura
            description: Condicação da Fatura a Pagar
"""
