import pandas as pd
import os

def load_data(file_path):
    return pd.read_excel(file_path)

def process_data(df):
    df = df.copy()
    df['Quantidade'] = 0
    df['Total'] = 0
    return df

def load_fornecedores():
    return ["Fornecedor A", "Fornecedor B", "Fornecedor C"]

def load_orcamentos(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        # Cria um arquivo CSV vazio com as colunas apropriadas
        empty_df = pd.DataFrame(columns=["Numero", "Codigo", "Unid", "Resumo", "Descricao", "Preco Mediano (R$)", "Data", "Tipo de Composição", "Obra", "Fornecedor", "Data Orçamento", "Valor Total"])
        empty_df.to_csv(file_path, index=False)
    return pd.read_csv(file_path)

def save_orcamento(df, file_path):
    df.to_csv(file_path, index=False, mode='a', header=not os.path.exists(file_path))

def generate_orcamento_number():
    file_path = "L:\\VSCode\\PYTHON\\DIO\\Planilha_Cotacao_Excel\\data\\Orcamentos_Salvos.csv"
    orcamentos = load_orcamentos(file_path)
    return len(orcamentos) + 1
