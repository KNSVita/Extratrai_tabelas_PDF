import tkinter as tk
from tkinter import filedialog
from extrator import extrair_tabela, salvar_excel

def obter_dados():
    caminho_PDF = filedialog.askopenfilename(title="Selecione o arquivo PDF")
    pagina_inicial = int(entrada_pagina_inicial.get())
    pagina_final = int(entrada_pagina_final.get())

    dados_por_pag = extrair_tabela(caminho_PDF, pagina_inicial, pagina_final)

    nome_arquivo_excel = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx")])
    salvar_excel(dados_por_pag, nome_arquivo_excel)

root = tk.Tk()
root.title("Extrair Tabela de PDF")

label_pagina_inicial = tk.Label(root, text="Página Inicial:")
label_pagina_inicial.grid(row=0, column=0)

entrada_pagina_inicial = tk.Entry(root)
entrada_pagina_inicial.grid(row=0, column=1)

label_pagina_final = tk.Label(root, text="Página Final:")
label_pagina_final.grid(row=1, column=0)

entrada_pagina_final = tk.Entry(root)
entrada_pagina_final.grid(row=1, column=1)

botao_selecionar_pdf = tk.Button(root, text="Selecionar PDF", command=obter_dados)
botao_selecionar_pdf.grid(row=2, column=0, columnspan=2)

root.mainloop()

# fazer uma transposta
# fazer loading para o usuário 
