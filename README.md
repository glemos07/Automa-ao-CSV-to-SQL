CSV para SQL
Este projeto importa dados de arquivos CSV para um banco de dados SQLite. Ele também cria a tabela no banco de dados, caso ela não exista, e exibe os primeiros 10 nomes após a importação.

Funcionalidades
Conexão com Banco de Dados: Estabelece conexão com um banco SQLite.
Criação de Tabela: Cria a tabela no banco se não existir.
Importação de CSV: Lê arquivos CSV e insere dados no banco de dados.
Exibição de Dados: Exibe os primeiros 10 nomes inseridos no banco.

Como Usar:

Clone o repositório:
git clone https://github.com/seu-usuario/csv-para-sql.git

Instale as dependências:
pip install -r requirements.txt

Coloque os arquivos CSV na pasta csv_teste.

Execute o script:
python app.py

Estrutura do Projeto
.
├── app.py                # Código principal para importação e manipulação dos dados
├── csv_teste/            # Pasta onde os arquivos CSV devem ser colocados
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto

Dependências
pandas
sqlalchemy
