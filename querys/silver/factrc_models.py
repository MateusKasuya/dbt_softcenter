def get_yml_content(source: str) -> str:
    return f"""
version: 2  # Versão do esquema de metadados

models:
  - name: {source}_factrc # Nome do modelo
    description: "View Silver da FACTRC"  # Descrição do modelo
    columns:
      - name: id_fatura
        description: ID da Fatura - Primary Key

      - name: nroctrc
        description: Número CTRC - FK FRCTRC

      - name: ufctrc
        description: UF CTRC - FK FRCTRC

      - name: dataemissao
        description: Data emissão da Fatura

      - name: situacao
        description: Situação em que se encontra a Fatura

      - name: codfilemite
        description: Código Filial Emitente - FK TBFIL

      - name: codfilcobra
        description: Código Filial Cobrador - FK TBFIL

      - name: cgccpfdestina
        description: CPF/CNPJ Destinatário - FK TBCLI

      - name: cgccpfremete
        description: CPF/CNPJ Remetente - FK TBCLI

      - name: cgccpffatura
        description: CPF/CNPJ Fatura - FK TBCLI

      - name: codciddes
        description: Código Cidade Destino - FK TBCID

      - name: codpro
        description: Código Produto - FK TBPRO

      - name: pesofrete_ton
        description: Peso do frete em toneladas

      - name: vlrtotfrete
        description: Valor Total do frete

      - name: vlrpedagio
        description: Valor do Pedágio

      - name: vlrimposto
        description: Valor do Imposto
"""
