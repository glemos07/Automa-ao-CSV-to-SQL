import os
import pandas as pd
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError


def conectar_banco(url: str) -> Engine | None:
    """
    Conecta ao banco de dados.

    Args:
        url (str): URL do banco de dados.

    Returns:
        Engine | None: Objeto do SQLAlchemy ou None em caso de falha.
    """
    try:
        engine = create_engine(url)
        print("Conexão com o banco estabelecida!")
        return engine
    except Exception as e:
        print(f"Falha ao conectar ao bando de dados: {e}")
        return None


def verifica_tabela(engine: Engine, tabela: str) -> bool:
    """
    Verifica se a tabela já existe

    Args:
        engine (Engine): Objeto do SQLAlchemy
        tabela (str): Nome da tabela a verificar

    Returns:
        bool: Retorna True se existir no banco, caso contrário não.
    """

    inspetor = inspect(engine)

    return tabela in inspetor.get_table_names()


def cria_tabela(engine: Engine, tabela: str) -> None:
    """
    Cria tabela se não existir

    Args:
        engine (Engine): Objeto SQLAlchemy
        tabela (str): Tabela para verificar e criar.
    """

    if not verifica_tabela(engine, tabela):
        print(f"Tabela {tabela} não existe, criando a tabela")

        try:
            with engine.connect() as conn:
                conn.execute(
                    text(
                    f"""
                             CREATE TABLE {tabela}(
                             id INTEGER PRIMARY KEY,
                             nome TEXT,
                             idade INTEGER
                             )
                             """
                        )
                )
                conn.commit()
                print("Tabela criada com sucesso!")
        except OperationalError as e:
            print(f"Erro na criação da tabela: {e}")

def exibir_nomes(engine: Engine) -> None:
    """
    Faz um select e exibe os nomes

    Args:
        engine (Engine): Objeto do SQLAlchemy
    """
    query = "SELECT nome FROM dados_teste limit 10"

    with engine.connect() as conn:
        resultado = conn.execute(text(query))
        for row in resultado:
            print(row[0])




def importar_csv(
    caminho: str, engine: Engine, tabela: str, tamanho_csv: int = 10000
) -> None:
    """
    Importa os dados CSV para o banco de dados.

    Args:
        caminho (str): caminho dos arquivos CSV.
        engine (Engine): Objeto Engine do SQLAlchemy.
        tabela (str): nome da tabela que irá fazer o insert.
        tamanho_csv (int): tamanho máximo de linhas do CSV.

    Raises:
        FileNotFoundError: Caso o diretório não existir.
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError("O caminho informado não existe")
    
    cria_tabela(engine, tabela)

    for arquivo in os.listdir(caminho):
        if arquivo.endswith(".csv"):
            caminho = os.path.join(caminho, arquivo)
            print(f"Processando o arquivo: {arquivo}")

            try:
                for chunck in pd.read_csv(caminho, chunksize=tamanho_csv):
                    with engine.begin() as conn:
                        chunck.to_sql(
                            name=tabela,
                            con=conn,
                            if_exists="append",
                            index=False
                        )
            except Exception as e:
                print(f"Erro ao importar o arquivo {arquivo}: {e}")
                continue


def main():
    """
    Função princial para rodar as outras funções.
    """
    url_banco = "sqlite:///banco_teste.db"
    caminho_pasta = r"D:\Portfolio\automacoes\csv para sql\csv_teste"
    tabela = "dados_teste"

    engine = conectar_banco(url_banco)
    if not engine:
        print("Não foi possível conectar ao banco, encerrando script")
        exit(1)
    else:
        importar_csv(caminho_pasta, engine, tabela)
        print("Arquivos do CSV foram exportados para o banco de dados.\n")
        print("Este são os primeiros 10 nomes:\n")
        exibir_nomes(engine)


if __name__ == "__main__":
    main()