# Use a imagem do Python como base
FROM python:3.12.10-slim

# Define o diretório de trabalho no contêiner
WORKDIR /src

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Copia os arquivos do projeto para dentro do contêiner
COPY . .

# Instala dependências do Poetry
RUN poetry install --only main --no-root

# Garante a pasta e copia o profile pro local padrão do dbt
RUN mkdir -p /root/.dbt && \
    cp /src/profiles.yml /root/.dbt/profiles.yml

# Cria um script shell para executar os comandos dbt
RUN echo '#!/bin/bash\npoetry run dbt run\npoetry run dbt test' > /src/run_dbt.sh && \
    chmod +x /src/run_dbt.sh

# Define o comando padrão para rodar o script
CMD ["/src/run_dbt.sh"]