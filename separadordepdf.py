import PyPDF2

def separar_paginas(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        writer = PyPDF2.PdfWriter()

        for i in range(len(reader.pages)):
            page = reader.pages[i]
            width = page.mediabox.width
            height = page.mediabox.height

            # Criar página esquerda
            esquerda = page.cropbox.lower_left = (0, 0)
            page.cropbox.upper_right = (width / 2, height)
            writer.add_page(page)

            # Criar página direita
            direita = reader.pages[i]  # Clonar a página original
            direita.cropbox.lower_left = (width / 2, 0)
            direita.cropbox.upper_right = (width, height)
            writer.add_page(direita)

        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

# Exemplo de uso
input_pdf_path = 'entrada.pdf'  # Arquivo de entrada
output_pdf_path = 'pdf_separado.pdf'  # Arquivo de saída
separar_paginas(input_pdf_path, output_pdf_path)
