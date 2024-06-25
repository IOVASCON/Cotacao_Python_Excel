# Sistema de Orçamento de Compras

## Descrição

Este projeto é um sistema de orçamento de compras desenvolvido em Python utilizando as bibliotecas pandas e tkinter. O sistema permite a leitura de uma planilha Excel com dados de insumos, a visualização desses insumos em uma interface gráfica, a seleção de insumos e a geração de um relatório de orçamento.

## Funcionalidades

    Leitura de dados de insumos a partir de uma planilha Excel.
    Exibição dos insumos em uma interface gráfica com opção de seleção.
    Geração de um relatório de orçamento com os insumos selecionados e cálculo do valor total.
    Salvamento do orçamento gerado em um arquivo CSV para posterior consulta.

## Estrutura do Projeto

├── data
│   ├── Precos_Insumos.xlsx
│   ├── Orcamentos_Salvos.csv
├── src
│   ├── data_processing.py
│   ├── gui.py
│   ├── main.py
└── README.md

## Instalação

    1. Clone o repositório:

    git clone <url-do-repositorio>

    cd <nome-do-repositorio>

    2. Crie um ambiente virtual (opcional, mas recomendado):

    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`

    3. Instale as dependências:

    pip install -r requirements.txt

## Execução

    1. Certifique-se de que o arquivo Orcamentos_Salvos.csv esteja presente na pasta data e esteja vazio ou com a estrutura correta.

    2. Execute o arquivo main.py:

        python src/main.py

    3. Utilize a interface gráfica para selecionar os insumos desejados e gerar o relatório de orçamento.

## Uso

    1. Inicie a aplicação executando o arquivo main.py.
    2. Na interface gráfica, preencha os campos "Obra", "Fornecedor" e "Data".
    3. Selecione os insumos desejados na tabela.
    4. Clique no botão "Criar Relatório Orçamento" para gerar o relatório com os itens selecionados.
    5. O relatório será exibido em uma nova janela e o orçamento será salvo no arquivo Orcamentos_Salvos.csv

## Dependências

    Python 3.10 ou superior
    pandas
    tkinter
