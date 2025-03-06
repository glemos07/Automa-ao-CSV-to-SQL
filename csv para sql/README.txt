
# Automação CSV para SQL

Este projeto tem como objetivo automatizar o processo de importação de arquivos CSV para um banco de dados SQLite utilizando SQLAlchemy. A automação verifica a existência da tabela no banco, cria a tabela se necessário, e importa os dados dos arquivos CSV para a tabela especificada.

## Funcionalidades
- Conexão com o banco de dados SQLite.
- Verificação e criação da tabela no banco.
- Importação de arquivos CSV para a tabela no banco de dados.
- Exibição dos dados inseridos.

## Requisitos
- Python 3.x
- Bibliotecas necessárias:
  - pandas
  - sqlalchemy

## Como Usar

1. Clone ou baixe o repositório.
2. Instale as dependências com o comando:

    ```bash
    pip install -r requirements.txt
    ```

3. Altere o caminho do diretório onde os arquivos CSV estão localizados e a URL do banco de dados SQLite na função `main()`.
4. Execute o script `app.py`:

    ```bash
    python app.py
    ```

O script irá conectar ao banco de dados, criar a tabela (caso não exista), e importar os dados dos arquivos CSV para o banco.

## Autor
Guilherme Lemos Freitas
