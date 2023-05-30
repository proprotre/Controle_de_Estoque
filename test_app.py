import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import Produto, adicionar_produto


# Configuração do banco de dados de teste
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()

# Fixture para criar uma tabela temporária no banco de dados de teste
@pytest.fixture(scope="module")
def create_database():
    Produto.metadata.create_all(engine)
    yield
    Produto.metadata.drop_all(engine)

# Função para adicionar um produto
def adicionar_produto(session, nome, valor_compra, valor_venda, quantidade):
    produto = Produto(nome=nome, valor_compra=valor_compra, valor_venda=valor_venda, quantidade=quantidade)
    session.add(produto)
    session.commit()
    print("Produto adicionado com sucesso!")

# Teste para a função adicionar_produto
def test_adicionar_produto(create_database):
    # Dados do produto de teste
    nome = "Teste"
    valor_compra = 10
    valor_venda = 20
    quantidade = 5

    # Chama a função adicionar_produto passando a sessão
    adicionar_produto(session, nome, valor_compra, valor_venda, quantidade)

    # Verifica se o produto foi adicionado corretamente
    produto = session.query(Produto).first()
    assert produto.nome == nome
    assert produto.valor_compra == valor_compra
    assert produto.valor_venda == valor_venda
    assert produto.quantidade == quantidade
