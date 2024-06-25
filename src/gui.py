import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from data_processing import load_data, process_data, save_orcamento, generate_orcamento_number, load_fornecedores
from datetime import datetime

class Application(tk.Tk):
    def __init__(self, data, orcamento_file):
        super().__init__()
        self.title("Sistema de Orçamento")
        self.geometry("1200x600")
        self.orcamento_file = orcamento_file

        # Campos adicionais
        self.label_obra = tk.Label(self, text="Obra:")
        self.label_obra.pack()
        self.entry_obra = tk.Entry(self)
        self.entry_obra.pack()

        self.label_fornecedor = tk.Label(self, text="Fornecedor:")
        self.label_fornecedor.pack()
        self.combo_fornecedor = ttk.Combobox(self, values=load_fornecedores())
        self.combo_fornecedor.pack()

        self.label_data = tk.Label(self, text="Data:")
        self.label_data.pack()
        self.entry_data = tk.Entry(self)
        self.entry_data.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_data.pack()

        # Treeview para seleção de insumos com grade e bordas
        columns = ['Código', 'Unid', 'Resumo', 'Descriçao do Insumo', 'Preço Mediano (R$)', 'Data', 'Tipo de Composição']
        self.tree = ttk.Treeview(self, columns=columns, show='headings', selectmode='extended')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Definir colunas
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=100, anchor='center')

        self.tree.tag_configure('odd', background='#E8E8E8')
        self.tree.tag_configure('even', background='#DFDFDF')

        # Adicionar dados
        for i, row in data.iterrows():
            values = list(row)
            tag = 'odd' if i % 2 == 0 else 'even'
            self.tree.insert("", "end", values=values, tags=(tag,))

        # Botão para criar relatório de orçamento
        create_report_button = tk.Button(self, text="Criar Relatório Orçamento", command=self.create_report)
        create_report_button.pack()

    def create_report(self):
        selected_items = []
        for item in self.tree.selection():
            values = self.tree.item(item, "values")
            selected_items.append(values)

        if not selected_items:
            messagebox.showwarning("Aviso", "Nenhum item selecionado.")
            return

        obra = self.entry_obra.get()
        fornecedor = self.combo_fornecedor.get()
        data = self.entry_data.get()

        if not obra or not fornecedor or not data:
            messagebox.showwarning("Aviso", "Preencha todos os campos antes de criar o relatório.")
            return

        orcamento = []
        numero = generate_orcamento_number()
        valor_total = 0

        for item in selected_items:
            codigo, unid, resumo, descricao, preco_mediano, data_insumo, tipo_composicao, *_ = item  # Use o operador de desempacotamento
            preco_mediano = float(preco_mediano.replace(",", "."))  # Corrige a conversão de string para float
            orcamento.append({
                "Numero": numero,
                "Codigo": codigo,
                "Unid": unid,
                "Resumo": resumo,
                "Descricao": descricao,
                "Preco Mediano (R$)": preco_mediano,
                "Data": data_insumo,
                "Tipo de Composição": tipo_composicao,
                "Obra": obra,
                "Fornecedor": fornecedor,
                "Data Orçamento": data,
                "Valor Total": 0  # Inicializando com zero, será atualizado depois
            })
            valor_total += preco_mediano

        for o in orcamento:
            o["Valor Total"] = valor_total

        save_orcamento(pd.DataFrame(orcamento), self.orcamento_file)
        self.show_report(orcamento, valor_total)

    def show_report(self, orcamento, valor_total):
        report_window = tk.Toplevel(self)
        report_window.title("Relatório de Orçamento")
        report_window.geometry("800x600")

        text = tk.Text(report_window)
        text.pack(fill=tk.BOTH, expand=True)

        text.insert(tk.END, "ORÇAMENTO DE COMPRAS\n\n")
        for item in orcamento:
            text.insert(tk.END, f"{item['Codigo']}, {item['Unid']}, {item['Resumo']}, {item['Descricao']}, {item['Preco Mediano (R$)']}, {item['Data']}, {item['Tipo de Composição']}\n")

        text.insert(tk.END, f"\nValor Total: {valor_total:.2f}")

def main():
    data_file = "L:\\VSCode\\PYTHON\\DIO\\Planilha_Cotacao_Excel\\data\\Precos_Insumos.xlsx"
    orcamento_file = "L:\\VSCode\\PYTHON\\DIO\\Planilha_Cotacao_Excel\\data\\Orcamentos_Salvos.csv"
    df = load_data(data_file)
    processed_data = process_data(df)
    app = Application(processed_data, orcamento_file)
    app.mainloop()

if __name__ == "__main__":
    main()
