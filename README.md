# Sistema de Gerenciamento de Produtos

Este projeto consiste em um sistema de gerenciamento de produtos, desenvolvido em Python utilizando o SQLAlchemy para interação com o banco de dados SQLite.

## Ambiente de Desenvolvimento

Para desenvolver e executar a aplicação, você precisará de um ambiente com as seguintes dependências:

- Python 3.x
- SQLAlchemy
- SQLite

## Instalação e Execução

Siga as etapas abaixo para configurar e executar a aplicação:

1. Clone o repositório para o seu ambiente de desenvolvimento:

   ```
   git clone https://github.com/proprotre/Controle_de_Estoque
   ```

2. Acesse o diretório do projeto:

   ```
   cd Controle_de_Estoque
   ```

3. Crie um ambiente virtual (opcional):

   ```
   python -m venv venv
   ```

4. Ative o ambiente virtual (opcional):

   - Windows:

     ```
     venv\Scripts\activate
     ```

   - Unix/macOS:

     ```
     source venv/bin/activate
     ```

5. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

6. Execute a aplicação:

   ```
   python app.py
   ```

A aplicação será iniciada e você poderá interagir com as opções do menu.

## Testes Automatizados

Para garantir a qualidade do código e evitar regressões, foram implementados testes automatizados utilizando a biblioteca "pytest". 

Para executar os testes, certifique-se de ter o "pytest" instalado. Caso contrário, você pode instalá-lo com o comando "pip install pytest".

Para executar os testes automatizados, siga as etapas abaixo:

1. Certifique-se de estar no diretório raiz do projeto.

2. Execute o seguinte comando:

   ```
   pytest -s test_app.py
   ```

   O "pytest" irá descobrir automaticamente os testes definidos nos arquivos "test_*.py" presentes no projeto e executá-los. A saída do teste indicará se eles passaram ou falharam.

## Requisitos de Sistema

Para executar a aplicação, é necessário ter o Python 3.x instalado no seu sistema.

## Contribuição

Se desejar contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork do repositório.

2. Crie uma branch para a sua nova funcionalidade:

   ```
   git checkout -b minha-nova-funcionalidade
   ```

3. Faça as alterações necessárias e adicione os commits:

   ```
   git commit -m "Minha nova funcionalidade"
   ```

4. Faça o push para o seu repositório fork:

   ```
   git push origin minha-nova-funcionalidade
   ```

5. Abra um pull request no repositório original, descrevendo as alterações propostas.

## Práticas de Código Limpo

Neste projeto, foram aplicadas as seguintes práticas de código limpo:

- Uso de nomes de variáveis, funções e classes descritivos e significativos.
- Organização do código em funções e classes para melhor legibilidade e manutenibilidade.
- Uso de comentários para explicar trechos de código complexos ou importantes.
- Estruturação do código em blocos e indentação adequada para facilitar a leitura.

## Padrão de Projeto de Software

Neste projeto, foi utilizado o padrão de projeto de software conhecido como Active Record. O modelo "Produto" representa a tabela do banco de dados e possui os métodos para interação com os dados, como adicionar, atualizar e excluir produtos.

## Autor
Gabriel Badaró
