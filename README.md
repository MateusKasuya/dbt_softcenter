# dbt_softcenter

## Enums

O arquivo `src/utils/enums.py` contém classes de enumeração que são utilizadas para padronizar valores em todo o projeto. Abaixo está a descrição de cada enum:

### Source
Enumeração que representa as fontes de dados disponíveis:
- `FN9`: Representa a fonte FN9
- `MGP`: Representa a fonte MGP
- `RCR`: Representa a fonte RCR

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

# DBT Model Generator

Este projeto é um gerador de modelos DBT que cria automaticamente arquivos SQL e YML para diferentes camadas (bronze, silver e gold) baseado em fontes de dados configuradas.

## Estrutura do Projeto

```
.
├── models/
│   ├── bronze/     # Configurações de fonte
│   ├── silver/     # Modelos da camada silver
│   └── gold/       # Modelos da camada gold
├── querys/         # Templates de queries SQL e YML
└── src/
    └── utils/      # Utilitários e lógica do gerador
```

## Como Adicionar Novas Fontes ou Tabelas

### 1. Adicionando uma Nova Fonte (Source)

Para adicionar uma nova fonte de dados, siga estes passos:

1. Abra o arquivo `src/utils/enums.py`
2. Localize a classe `Source`
3. Adicione o novo enum seguindo o padrão existente:

```python
class Source(Enum):
    FN9 = "fn9"
    MGP = "mgp"
    RCR = "rcr"
    NOVA_FONTE = "nova_fonte"  # Adicione sua nova fonte aqui
```

4. Atualize a lista de fontes no arquivo `src/main.py`:

```python
list_of_sources = [Source.FN9, Source.MGP, Source.RCR, Source.NOVA_FONTE]
```

### 2. Adicionando uma Nova Tabela

Para adicionar uma nova tabela ao sistema, siga estes passos:

1. Abra o arquivo `src/utils/enums.py`
2. Localize a classe `Table`
3. Adicione o novo enum seguindo o padrão existente:

```python
class Table(Enum):
    FRCTRC = "frctrc"
    CPTIT = "cptit"
    # ... outras tabelas ...
    NOVA_TABELA = "nova_tabela"  # Adicione sua nova tabela aqui
```

4. Crie os arquivos de template para a nova tabela:

   a. Para tabelas Silver:
   - Crie `querys/silver/nova_tabela.py` com a função `get_query_content()`
   - Crie `querys/silver/nova_tabela_models.py` com a função `get_yml_content()`

   b. Para tabelas Gold:
   - Crie `querys/gold/nova_tabela_yml.py` com a função `get_yml_content()`
   - Adicione a lógica para a nova tabela em `querys/gold/sql.py`

5. Atualize a lista de tabelas em `src/utils/silver_models.py` e `src/utils/gold_models.py`:

```python
list_of_tables = [
    Table.CPTIT,
    Table.FACTRC,
    # ... outras tabelas ...
    Table.NOVA_TABELA,  # Adicione sua nova tabela aqui
]
```

6. Adicione a lógica de processamento específica para a nova tabela nos arquivos:
   - `src/utils/silver_models.py`
   - `src/utils/gold_models.py`

## Exemplo de Implementação

### 1. Adicionando uma Nova Fonte

```python
# src/utils/enums.py
class Source(Enum):
    FN9 = "fn9"
    MGP = "mgp"
    RCR = "rcr"
    NOVA_FONTE = "nova_fonte"

# src/main.py
list_of_sources = [Source.FN9, Source.MGP, Source.RCR, Source.NOVA_FONTE]
```

### 2. Adicionando uma Nova Tabela

```python
# src/utils/enums.py
class Table(Enum):
    FRCTRC = "frctrc"
    CPTIT = "cptit"
    NOVA_TABELA = "nova_tabela"

# src/utils/silver_models.py
if table == Table.NOVA_TABELA:
    yml_content = nova_tabela_yml(source.value)
    sql_content = nova_tabela_sql(source.value)
```

## Executando o Gerador

Após adicionar as novas variáveis, execute o gerador:

```bash
python src/main.py
```

O gerador irá criar automaticamente todos os arquivos necessários para as novas fontes e tabelas adicionadas.

## Notas Importantes

1. Mantenha a consistência nos nomes dos arquivos e funções
2. Siga o padrão de nomenclatura existente
3. Certifique-se de que todos os templates necessários foram criados
4. Teste a geração com uma nova fonte/tabela antes de adicionar várias
5. Mantenha a documentação atualizada ao adicionar novas funcionalidades
