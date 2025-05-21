# dbt_softcenter

## Enums

O arquivo `src/utils/enums.py` contém classes de enumeração que são utilizadas para padronizar valores em todo o projeto. Abaixo está a descrição de cada enum:

### Source
Enumeração que representa as fontes de dados disponíveis:
- `FN9`: Representa a fonte FN9
- `MGP`: Representa a fonte MGP
- `RCR`: Representa a fonte RCR

### Schema
Enumeração que representa os schemas do banco de dados:
- `SILVER`: Representa o schema silver
- `GOLD`: Representa o schema gold

### Table
Enumeração que representa as tabelas do sistema:
- `FRCTRC`: Tabela de faturamento
- `CPTIT`: Tabela de cupom fiscal
- `FACTRC`: Tabela de faturamento
- `TBCID`: Tabela de cidades
- `TBCLI`: Tabela de clientes
- `TBFIL`: Tabela de filiais
- `TBFOR`: Tabela de fornecedores
- `TBHIS`: Tabela de histórico
- `TBPRO`: Tabela de produtos
- `TBCTA`: Tabela de contas

### Como usar

Para utilizar estas enumerações em seu código, importe-as da seguinte forma:

```python
from src.utils.enums import Source, Schema, Table

# Exemplo de uso
source = Source.FN9
schema = Schema.SILVER
table = Table.TBCLI
```

Os valores das enumerações podem ser acessados através do atributo `value`:

```python
source_value = Source.FN9.value  # retorna "fn9"
schema_value = Schema.SILVER.value  # retorna "silver"
table_value = Table.TBCLI.value  # retorna "TBCLI"
```

## Como Adicionar Novas Enumerações

O arquivo `src/utils/enums.py` contém as enumerações utilizadas no projeto. Para adicionar uma nova enumeração, siga os passos abaixo:

### 1. Estrutura Básica
Todas as enumerações devem herdar da classe `Enum` do Python e seguir o padrão:

```python
class NomeDaEnum(Enum):
    VALOR1 = "valor1"
    VALOR2 = "valor2"
```

### 2. Passos para Adicionar uma Nova Enumeração

1. Abra o arquivo `src/utils/enums.py`
2. Adicione a nova classe de enumeração seguindo o padrão existente
3. Cada valor da enumeração deve ser definido como uma constante com seu respectivo valor string
4. Mantenha os valores em minúsculo para consistência com o padrão existente

### Exemplo de Adição

```python
# Antes
class Source(Enum):
    FN9 = "fn9"
    MGP = "mgp"
    RCR = "rcr"

# Depois de adicionar uma nova fonte
class Source(Enum):
    FN9 = "fn9"
    MGP = "mgp"
    RCR = "rcr"
    NOVA = "nova"  # Nova fonte adicionada
```

### Boas Práticas

1. Mantenha os nomes das enumerações em inglês
2. Use nomes descritivos para as constantes
3. Mantenha os valores em minúsculo
4. Adicione comentários explicativos quando necessário
5. Mantenha a ordem alfabética dos valores dentro de cada enumeração
6. Atualize a documentação quando adicionar novas enumerações

### Observações Importantes

- Evite modificar valores existentes, pois isso pode quebrar código que já utiliza essas enumerações
- Se precisar remover uma enumeração, verifique primeiro se ela não está sendo utilizada em outras partes do código
- Ao adicionar uma nova enumeração, certifique-se de que ela segue o mesmo padrão das existentes
