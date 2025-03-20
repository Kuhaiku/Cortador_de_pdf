import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def separar_paginas(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        writer = PyPDF2.PdfWriter()

        for i in range(len(reader.pages)):
            page = reader.pages[i]
            width = page.mediabox.width
            height = page.mediabox.height

            # Página esquerda
            page.cropbox.lower_left = (0, 0)
            page.cropbox.upper_right = (width / 2, height)
            writer.add_page(page)

            # Página direita (a partir da mesma página original)
            direita = reader.pages[i]  # Sem cópia
            direita.cropbox.lower_left = (width / 2, 0)
            direita.cropbox.upper_right = (width, height)
            writer.add_page(direita)

        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

def escolher_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if arquivo:
        entrada_var.set(arquivo)

def salvar_arquivo():
    arquivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Arquivos PDF", "*.pdf")])
    if arquivo:
        saida_var.set(arquivo)

def processar():
    entrada = entrada_var.get()
    saida = saida_var.get()
    if not entrada or not saida:
        messagebox.showerror("Erro", "Selecione os arquivos de entrada e saída.")
        return
    try:
        separar_paginas(entrada, saida)
        messagebox.showinfo("Sucesso", "PDF separado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o PDF:\n{e}")

# Interface
janela = tk.Tk()
janela.title("Separador de Páginas PDF (Esquerda/Direita)")
janela.geometry("500x200")

entrada_var = tk.StringVar()
saida_var = tk.StringVar()

tk.Label(janela, text="PDF de Entrada:").pack(pady=5)
tk.Entry(janela, textvariable=entrada_var, width=50).pack()
tk.Button(janela, text="Selecionar Arquivo", command=escolher_arquivo).pack(pady=5)

tk.Label(janela, text="PDF de Saída:").pack(pady=5)
tk.Entry(janela, textvariable=saida_var, width=50).pack()
tk.Button(janela, text="Salvar Como", command=salvar_arquivo).pack(pady=5)

tk.Button(janela, text="Separar Páginas", command=processar, bg="green", fg="white").pack(pady=10)

janela.mainloop()
