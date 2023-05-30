from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria o engine de conexão com o banco de dados
engine = create_engine("sqlite:///produtos.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Classe Produto para mapear a tabela do banco de dados
class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    valor_compra = Column(Integer)
    valor_venda = Column(Integer)
    quantidade = Column(Integer)

    def __repr__(self):
        return f"Produto ID: {self.id} | Nome: '{self.nome}' | Valor de compra: R${self.valor_compra} | Valor de venda: R${self.valor_venda} | Quantidade: {self.quantidade}un"

# Cria a tabela no banco de dados (caso não exista)
Base.metadata.create_all(engine)

# Função para adicionar um produto
def adicionar_produto(nome, valor_compra, valor_venda, quantidade):
    if nome and valor_compra and valor_venda and quantidade != "":
        produto = Produto(nome=nome, valor_compra=valor_compra, valor_venda=valor_venda, quantidade=quantidade)
        session.add(produto)
        session.commit()
        print("Produto adicionado com sucesso!")
    else:
        print("Você não pode adicionar valores vazios!")

# Função para ler todos os produtos
def ler_produtos():
    produtos = session.query(Produto).all()
    for produto in produtos:
        print(produto)
    if produtos == []:
        print("Sem produtos no estoque!")

# Função para atualizar um produto
def atualizar_produto():
    try:
        produto_id = int(input("Digite o ID do produto: "))
        produto = session.get(Produto, produto_id)
        if produto:
            nome = input("Digite um novo nome: ")
            valor_compra = input("Digite um novo valor de compra: ")
            valor_venda = input("Digite um novo valor de venda: ")
            quantidade = input("Digite uma nova quantidade: ")         
            if nome and valor_compra and valor_venda and quantidade != "":
                produto.nome = nome
                produto.valor_compra = valor_compra
                produto.valor_venda = valor_venda
                produto.quantidade = quantidade
                session.commit()
                print("Produto atualizado com sucesso!")
            else:
                print("Você não pode adicionar valores vazios!")
        else:
            print("Produto não encontrado!")
    except ValueError:
        print("Valor Inválido!")

# Função para excluir um produto
def excluir_produto():
    try:
        produto_id = int(input("Digite o ID do produto: "))
        produto = session.get(Produto, produto_id)
        if produto:
            session.delete(produto)
            session.commit()
            print("Produto excluído com sucesso!")
        else:
            print("Produto não encontrado!")
    except ValueError:
        print("Valor Inválido!")
# Função para solicitar um produto
def solicitar_produto():
    nome = input("Digite o nome do produto: ")
    valor_compra = input("Digite o valor de compra: ")
    valor_venda = input("Digite o valor de venda: ")
    qtd = input("Digite a quantidade adquirida: ")
    adicionar_produto(nome, valor_compra, valor_venda, qtd)

def menu():
    while True:
        try:
            print("\n==============================================")
            print("Escolha uma opção:\n1- Cadastrar Produto\n2- Editar Produto\n3- Excluir Produto\n4- Listar Produtos\n5- Sair")
            print("==============================================\n")
            opcao = int(input("Digite uma opção: "))
            print("\n")
            if opcao == 1:
                solicitar_produto()
            elif opcao == 2:
                atualizar_produto()
            elif opcao == 3:
                excluir_produto()
            elif opcao == 4:
                ler_produtos()
            elif opcao == 5:
                print("Você encerrou o sistema!")
                break
        except ValueError:
            print("\n==============================================")
            print("Opção Inválida!")
            print("==============================================")

menu()
